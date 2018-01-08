if __name__ == '__main__':
	list1 = []
	inner_list = []
	marksheet = []
	for _ in range(int(input())):
		marksheet.append([input(), float(input())])
	second_lowest = sorted(list(set([marks for name, marks in marksheet])))[1]
	for name, marks in sorted(marksheet):
		if marks == second_lowest:
			print(name)
