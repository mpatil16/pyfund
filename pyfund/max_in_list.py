def max_in_list(x):
	l = []
	for item in str(x):
		l.append(item)
	l = list(map(int, l))
	max = 0
	for item in range(len(l)):
		if max<l[item]:
			max=l[item]
	print(max)


if __name__ == '__main__':
	x = int(input())
	max_in_list(x)