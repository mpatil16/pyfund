import sys
def generate_n_chars(n,c):
	for x in range(n):
		sys.stdout.write(c)


if __name__ == '__main__':
	n = int(input())
	c = sys.stdin.read(1)
	generate_n_chars(n,c)