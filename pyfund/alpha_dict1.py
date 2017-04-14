import string


def get_even_alpha():

    """ This method returns dictionary of alphabets with even values"""
    alpha = {}
    number = 1
    for x in string.ascii_lowercase:
        alpha[x] = number
        number += 1
    even_alpha = {x: alpha[x] for x in string.ascii_lowercase if (alpha[x] % 2 == 0)}
    print(even_alpha)

get_even_alpha()