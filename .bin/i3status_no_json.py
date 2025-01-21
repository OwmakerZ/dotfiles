#!/usr/bin/python3
import time
import subprocess
import subprocess
import threading
import queue

class mystatus:
    def __init__(self, i3_enable=True, i3_config="~/.config/i3status/i3status.conf"):
        self.modules = []
        if i3_enable:
            self.process = subprocess.Popen(['i3status', '-c',  i3_config], stdout=subprocess.PIPE,  stderr=subprocess.PIPE, text=True)
            self.modules.append( lambda: self.process.stdout.readline().strip())
        print( self.modules)

    def register(self, module, front=True):
        # module is a lambda
        if front:
            self.modules.insert(0, module)
        else:
            self.modules.append(module)

    def echo(self):
        status = ""
        for module in self.modules:
            status += module()
        print( status, flush=True)


if __name__ == '__main__':
    status = mystatus(i3_enable=False)
    status.register( lambda: '[' + subprocess.run(['/home/owmaker/.bin/get_window_class.sh'], text=True, capture_output=True).stdout.strip() + '] | ')
    while True:
        status.echo()
        time.sleep(0.5)
