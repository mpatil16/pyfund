import sys
def is_member(x,a):
	l=[]
	for item in a:
		l.append(item)
	length = len(l)
	is_true = False
	for item in range(length):
		if l[item] == x:
			is_true=True
			break
		else:
			is_true=False
	print(is_true)

if __name__ == '__main__':
	x = sys.stdin.read(1)
	a = input()
	is_member(x,a)
