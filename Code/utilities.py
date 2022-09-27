import math 
import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()

class Utilities:
    def __init__(self, os, user):
        self.os = os
        self.username = user
        import math
    
    def calculator(self, n1=0, n2=0, op='+'):
        try:
            if op == '+':
                return n1 + n2
            
            elif op == '-':
                return n1 - n2
            
            elif op == '*':
                return n1 * n2
            
            elif op == '/':
                try:
                    return n1/n2
                except:
                    return "Invalid"

            elif op == '^':
                return n1 ^ n2
            
            elif op == '/^':
                return n1 * (1/n2)
            
            elif op == '//':
                try:
                    return (n1//n2)
                except:
                    return "Invalid"
            
            elif op == 'sin':
                try:
                    return math.sin(n1)
                except:
                    return "Invalid"
            
            elif op == 'cos':
                try:
                    return math.cos(n1)
                except:
                    return "Invalid"
            
            elif op == 'tan':
                try:
                    return math.tan(n1)
                except:
                    return "Invalid"
            
            elif op == 'asin':
                try:
                    return math.asin(n1)
                except:
                    return "Invalid"
            
            elif op == 'acos':
                try:
                    return math.acos(n1)
                except:
                    return "Invalid"
            
            elif op == 'atan':
                try:
                    return math.atan(n1)
                except:
                    return "Invalid"
                
            elif op == 'abs':
                return abs(n1)
        except:
            return "Something went wrong"

    def notes(self, name=None, info='', append=True, read=True)->str:
        mode = 'a' if append else 'w'
        while True:
            try:
                try:
                    if read:
                        with open(f"{path}/OSData/Notes/{name}.txt", "r") as f:
                            return f.read()
                    else:
                        with open(f'{path}/OSData/Notes/{name}.txt', mode) as f:
                            f.write(info)
                            return "Changed"
                except:
                    try:
                        with open(f'{path}/OSData/Notes/{name}.txt', mode) as f:
                            continue
                    except:
                        return "Unable To Create File"
            except:
                return "Something went wrong"
                    
    def noteClear(self)->str:
        try:
            for f in os.listdir(f"{path}/OSData/Notes"):
                os.remove(os.path.join(f"{path}/OSData/Notes", f))
        except:
            return "Something went wrong"


u = Utilities('meOS', 'admin')
print(u.notes(name="a bored", info='test', append=False, read=False))
u.noteClear()