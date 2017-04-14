import string


def even_alpha():
    alpha = {}
    even_alphabets = {}
    all_alphabets = string.ascii_lowercase
    print(all_alphabets)
    number = 1
    for char in all_alphabets:
        alpha[char] = number
        number += 1
    print(alpha)
    keys = alpha.keys()
    for char in keys:
        if(alpha[char] % 2) == 0:
            even_alphabets[char] = alpha[char]
    print(even_alphabets)

if __name__ == '__main__':
    even_alpha()
