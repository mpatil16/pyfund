import sys
def histogram(x):
	l = []
	for item in str(x):
		l.append(item)
	length = len(l)
	l = list(map(int,l))
	for item in range(length):
		for var in range(l[item]):
			sys.stdout.write("*")
		print()


if __name__ == '__main__':
	x = int(input())
	histogram(x)
