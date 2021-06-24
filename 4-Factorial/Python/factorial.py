def factorial(num):
    num = int(num)
    if (num == 1):
        return num
    return num * factorial(num - 1)

if __name__ == '__main__':
    number = input('Please enter number: ')

    print(factorial(number))