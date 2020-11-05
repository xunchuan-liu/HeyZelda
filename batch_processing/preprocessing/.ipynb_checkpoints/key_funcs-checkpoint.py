file = open('shortcut_mac.in', 'r') 
Lines = file.readlines() 

count = 2
dict = {'Command(⌘)':'Key.cmd', 'Command':'Key.cmd', 'Ctrl': 'Key.ctrl', 'Control': 'Key.ctrl', 'Shift': 'Key.shift', 'Option': 'Key.alt'}
for line in Lines:
    if line == '\n':
        continue
        
    print('def t{}(self):'.format(count))
    keys = line.split(":", 1)[0].strip().split("+")
    for key in keys:
        if len(key) == 1:
            print("\tself.keyboard.press('{}')".format(key.lower()))
        else:
            print("\tself.keyboard.press({})".format(dict[key]))
            
    for key in keys:
        if len(key) == 1:
            print("\tself.keyboard.release('{}')".format(key.lower()))
        else:
            print("\tself.keyboard.release({})".format(dict[key]))
            
    count += 1
    print()