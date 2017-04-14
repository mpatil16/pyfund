l = [1,2,3,4]
def sum():
	result = 0
	length = len(l)
	for item in range(length):
		result=l[item]+result
	print("Addition of list:",result)


def multiply():
	result=1
	length=len(l)
	for x in range(length):
		result=l[x]*result
	print("Multipication of list:",result)


if __name__ == '__main__':
	sum()
	multiply()
