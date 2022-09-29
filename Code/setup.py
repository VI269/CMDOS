newname = ''
name = 'vedant iyer'
for letter in name:
    if letter == ' ': 
        newname+=('-')
    else:
        newname+=(letter)
    
print(newname)