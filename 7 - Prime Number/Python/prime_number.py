def checkPrime(number):

    check = True
    j = 2
    if (number <= 1):
        check = False
    
    while (j <= number/2): 
        if (number % j == 0):
            check = False
            break
        else:
            j += 1
    
    return check

if __name__ == '__main__':
    num = input('Input a number: ')
    if checkPrime(int(num)):
        print(f'{num} is prime number')
    else:
        print(f'{num} is NOT prime number')

