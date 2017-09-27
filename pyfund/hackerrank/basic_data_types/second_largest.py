def second_largest(arr):
	sorted_arr = sorted(arr)
	last_index = len(sorted_arr)
	maximum = sorted_arr[last_index-1]
	last_index = last_index-1

	while maximum == sorted_arr[last_index]:
		maximum = sorted_arr[-1]
		last_index = last_index-1
		second_large = sorted_arr[last_index]
	print(second_large)

if __name__ == '__main__':
	n = int(input())
	inputs = list(map(int, input().split()))[:n]
	second_largest(inputs)



"""Best way"""
# def second_largest(arr):
# 	maximum = max(arr)
# 	while max(arr) == maximum:
# 		arr.remove(max(arr))
# 	print(max(arr))