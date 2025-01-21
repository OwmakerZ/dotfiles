#!/usr/bin/python3
from time import sleep
import subprocess
print('{ "version": 1 }', flush=True)

# Begin the endless array.
print('[', flush=True)

print('[]', flush=True)

# Now send blocks with information forever:
while True:
    result = subprocess.run(['date'], capture_output=True, text=True).stdout
    wm     = subprocess.run(['./demo.sh'], capture_output=True, text=True).stdout
    print( ',[{"name":"time","full_text":"' + result.strip('\n') + '"},{"name":"Window","full_text":"' + wm.strip('\n') + '"}]', flush=True)
    sleep(0.5)
