
def list_operations(n):
	list_1 =[]
	for i in range(n):
		k = input().split()
		cmd = k[0]
		args = k[1:]
		if cmd != 'print':
			cmd+='('+','.join(args)+')'
			eval("list_1."+cmd)
		else:
			print(list_1)

if __name__ =='__main__':
	n = int(input())
	list_operations(n)
