def add(var1, var2):
    """This is add method."""
    return (var1+var2)


def subtract(var1, var2):
    """This is add method."""
    return (var1-var2)


if __name__ == '__main__':
    addition = add(int(input()), int(input()))
    print(addition)
    subtraction = subtract(int(input()), int(input()))
    print(subtraction)
