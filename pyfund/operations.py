list1 = ['3']
def operations(n):
	for num in range(n):
		s = input()
		if s == 'insert':
			i = input()
			e = input()
			list1[i] = e
		elif s == 'print':
			print(list1)
		elif s == 'remove':
			e = input()
			del list1[e]
		elif s == 'append':
			e = input()
			list1.append(e)
		elif s == 'sort':
			list1.sort()
		elif s == 'pop':
			list1.pop()
		elif s == 'reverse':
			list1.reverse()
			


if __name__ == '__main__':
	n = int(input())
	operations(n)