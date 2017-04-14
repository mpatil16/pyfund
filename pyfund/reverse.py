
def reverse_given_string(str1):
    l = []
    str1 = str1
    for x in str1:
        l.append(x)
        l.reverse()
    str2 = ''.join(l)
    print(str2)


if __name__ == '__main__':
    reverse_given_string(input())
