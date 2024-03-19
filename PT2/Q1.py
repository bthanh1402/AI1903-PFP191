def replace(inputlist):
    res = ''
    for i in range(len(inputlist[0])):
        if inputlist[0][i] == inputlist[1]:
            res +=  inputlist[2]
        else:
            res += inputlist[0][i]
    return res
while True:
    inputlist = input('Enter string and two chars (separate by ,): ').split(",")
    print('OUTPUT:', replace(inputlist))
    print('DONE')



