def overlapping(list1,list2):
	l1 = []
	l2 = []
	is_true = False
	for x in str(list1):
		l1.append(x)
	for x in str(list2):
		l2.append(x)
	l1 = list(map(int,l1))
	l2 = list(map(int,l2))
	length1 = len(l1)
	length2 = len(l2)
	for x in range(length1):
		for y in range(length2):
			if l1[x]==l2[y]:
				is_true = True
				break
			else:
				is_true = False
	if is_true==True:
		print("Overlapping")
	else:
		print("Not overlapping")



if __name__ == '__main__':
	list1 = int(input())
	list2 = int(input())
	overlapping(list1,list2)
