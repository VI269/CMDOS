import random

class Encryptor:
    chars = \
    {'∂', ')', '(', '@', '!', 'π', '$', '%', '&', ':', ';', '-', '+', '=', '^', '®', '`', '~', '"', "'",
        '>', '<', '?', '/', '}', 'w', 'x', '4', '5', 'k', ']', '\\', '|', 'o', 'p', 'v', 'ƒ', 'ø', '†', '¨',
        '∏', 'ß', 'µ', 'Â', 'Ω', 'Ï', 'å', '', 'Â', '≤', '≥'}
    chars = list(chars)
    bchar = chars
    def __init__(self):
        pass
    
    def encrypt(self, code, text):
        if code == '':
            for i in range(29):
                _item = random.choice(self.chars)
                code += _item
                self.chars.remove(_item)

        elif len(code) != 29:
            return None
        
        diction = {
            'a': code[0],
            'b': code[1],
            'c': code[2],
            'd': code[3],
            'e': code[4],
            'f': code[5],
            'g': code[6],
            'h': code[7],
            'i': code[8],
            'j': code[9],
            'k': code[10],
            'l': code[11],
            'm': code[12],
            'n': code[13],
            'o': code[14],
            'p': code[15],
            'q': code[16],
            'r': code[17],
            's': code[18],
            't': code[19],
            'u': code[20],
            'v': code[21],
            'w': code[22],
            'x': code[23],
            'y': code[24],
            'z': code[25],
            ' ': code[26],
            '.': code[27],
            ',': code[28]
        }
        for letter in text:
            coded += diction[letter]
        return coded
    
    def encrypt(self, code, text):
        if code == '':
            for i in range(29):
                _item = random.choice(self.chars)
                code += _item
                self.chars.remove(_item)

        elif len(code) != 29:
            return None
        
        diction = {
            'a': code[0],
            'b': code[1],
            'c': code[2],
            'd': code[3],
            'e': code[4],
            'f': code[5],
            'g': code[6],
            'h': code[7],
            'i': code[8],
            'j': code[9],
            'k': code[10],
            'l': code[11],
            'm': code[12],
            'n': code[13],
            'o': code[14],
            'p': code[15],
            'q': code[16],
            'r': code[17],
            's': code[18],
            't': code[19],
            'u': code[20],
            'v': code[21],
            'w': code[22],
            'x': code[23],
            'y': code[24],
            'z': code[25],
            ' ': code[26],
            '.': code[27],
            ',': code[28]
        }

        for letter in text:
            coded += list(diction.keys())[list(diction.values()).index(letter)]
        return coded
