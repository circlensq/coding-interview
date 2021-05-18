def palindromeCheck(args):
    if args == args[::-1]:
        return True
    return False

if __name__ == '__main__':
    word = input("Enter word: ")
    
    if palindromeCheck(word):
        print(word, 'is Palindrome')
    else:
        print(word, 'is NOT Palindrome')