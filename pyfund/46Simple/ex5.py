import string

all_letters = string.ascii_letters
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [var for var in all_letters if var not in vowels]


def consonant(str1):
    result = ""
    for char in str1:
        if char.lower() in consonants:
            result += char+"o"+char
        else:
            result += char
    return result


if __name__ == '__main__':
    print(consonant("This is robber's language"))
