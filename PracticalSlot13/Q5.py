inputline = input('The output for the input line:').strip()

count = {}
for char in inputline:
    if 'a' <= char < 'z':
        count[char] = count.get(char,0)  + 1

for key,value in count.items():
    print('The letter',key, 'appears',value, 'time(s)')
    