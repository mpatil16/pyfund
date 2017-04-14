import arithmatic1
def test_add():
	result = arithmatic1.add(4,3)
	assert(7 == result)


def test_subtract():
	result = arithmatic1.subtract(7,2)
	assert(5 == result)


if __name__ == '__main__':
	test_add()
	test_subtract()
	