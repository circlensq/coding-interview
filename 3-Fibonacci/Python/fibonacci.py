def fibonacci(number):
    number = int(number)
    if number == 1 or number == 0:
        return number
    
    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == '__main__':
    """
    Fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21
    Fibonacci of index 6 is 8
    """
    num = input('Number: ')

    print('Fibonacci of index', num, 'is', fibonacci(num))