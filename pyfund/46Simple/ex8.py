import sys


def palindrome(str):
    return str == str[::-1]

if __name__ == '__main__':
    print(palindrome("radar"))