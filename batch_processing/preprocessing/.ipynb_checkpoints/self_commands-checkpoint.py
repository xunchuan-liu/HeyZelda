file = open('shortcut_mac.in', 'r') 
Lines = file.readlines() 

print("self.commands = {")
count = 2
for line in Lines:
    if line == '\n':
        continue
    print('\t{}: "{}",'.format(count, line.split(":", 1)[-1].strip()))
    count += 1
print("}")