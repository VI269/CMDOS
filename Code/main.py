import os
import random
import platform
from utilities import Utilities

setup = False
util = Utilities()

username = ''

def refresh():
    global setup
    global username
    with open(f'{util.get_path()}/setup.txt', 'r') as f:
        setup = f.read()
    with open(f'{util.get_path()}/data.txt', 'r') as f:
        username = f.read()
    if username == 'anonymous': 
        with open(f'{util.get_path()}/setup.txt', 'w') as f:
            f.write(False)

def clearConsole():
    os.system("clear")

clearConsole()
refresh()

while True:
    cmd = input(f"{username}@{platform.system()} ~ $ ")
    try:
        if cmd == 'clear': 
            clearConsole()
        
        elif cmd == 'refresh':
            refresh()
        
        elif cmd == 'setup': 
            name = input('Name {anonymous} ~ $ ')
            newname = ''
            for letter in name:
                if letter == ' ': 
                    newname+=('-')
                else:
                    newname+=(letter)
            with open(f"{util.get_path()}/data.txt", 'w') as f:
                f.write(newname)
            with open(f"{util.get_path()}/setup.txt", 'w') as f:
                f.write(True)
        
        if setup:
            pass
    except:
        print("Something went wrong")