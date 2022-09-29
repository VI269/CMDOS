import os
# For the appmaker, run
class App:
    name = ''
    path = ''
    def __init__(self, name='', code_path=''):
        self.name = name
        self.path = code_path
    
    def joinToMain(self):
        pass