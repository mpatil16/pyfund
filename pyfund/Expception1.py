def test_exception():
    try:
        x = 3//0
        print(x)
    except ArithmeticError:
        print("Arithmetic Exception occured")


test_exception()