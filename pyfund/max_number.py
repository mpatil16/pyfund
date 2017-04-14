def max(x,y):
	if x>y:
		print("x is greater than y")
	else:
		print("y is greater than x")


def max_of_three(x,y,z):
	if (x>y) and (x>z):
		print("Maximum number is: "+str(x))
	elif (y>x) and (y>z):
		print("Maximum number is: "+str(y))
	else:
		print("Maximum number is: "+str(z))


if __name__ == '__main__':
	print("2 or 3:")
	a = int(input())
	if (a == 2):
		x = int(input())
		y = int(input())
		max(x,y)
	elif (a == 3):	
		x = int(input())
		y = int(input())
		z = int(input())
		max_of_three(x,y,z)
	