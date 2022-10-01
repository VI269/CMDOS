import os
import random
import platform
from utilities import Utilities

setup = False
util = Utilities()

username = open(f'{util.get_path()}/setup.txt', 'r').read()

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

setup_req_commands = ["notes", 'games', 'encryptor']

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
            if name.rstrip() == '': 
                name == 'anonymous'
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
        
        if cmd in setup_req_commands:
            if setup:
                if cmd == 'notes': 
                    _name = input("Enter note name ? ").lower().replace(' ', '-')
                    try:
                        clear = bool(input('Clear the note ? '))
                    except:
                        print('Enter a boolean value(True or False)')
                        continue
                    try:
                        _read = bool(input('Read note ? '))
                    except:
                        print('Enter a boolean value(True or False)')
                        continue
                    if not _read:
                        try:
                            _append = bool(input('Append or write to the note ? '))
                        except:
                            print('Enter a boolean value(True or False)')
                            continue
                        data = input("Data to enter in the note ? ")
                        print(util.notes(name=_name, info=data, append=_append, read=True))
                    else:
                        data = input("Data to enter in the note ? ")
                        print(util.notes(name=_name, info=data, append=_append, read=False))   
            else:
                print("Please setup user first.")
    except:
        print("Something went wrong")