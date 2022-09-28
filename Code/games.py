import random

class Games:
    osname = ''
    username = ''
    def __init__(self, os='myOS', name='Anonymous'):
        self.osname = os
        self.username = name
    
    def setupText(self)->str:
        return "OS: %s" % self.osname + "Username: %s" % self.username
    
    def rngNum():
        try:
            run = True
            while run:
                rnum = int(input("Enter a random number between 1 and 100: "))
                rcor = random.randint(1,100)
                if rnum > rcor:
                    print("Your guess was too high")
                    continue
                elif rnum < rcor:
                    print("Your guess was too low")
                    continue
                else:
                    print('You got it right')
                    run = False
            else: 
                print("Game Ended")
                return
        except:
            return "Something went wrong"
