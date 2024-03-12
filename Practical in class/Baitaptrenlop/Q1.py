def checkprime(x):
    if (x == 1):
        return False
    for n in range(2,x):
        if x % n == 0:
            return False
    return True
try:
    lst = list(map(int, input('Enter a sequence of positive integers:').split()))    
    max_prime = lst[0]
    print('The prime numbers are: ', end = '')
    for x in lst:
        if checkprime(x):
            print (x,end = ' ')
            if (x > max_prime):
                max_prime = x
    print('\nThe largest prime number:', max_prime)    
except:
    print('The input must be a sequence of positive integers!')


