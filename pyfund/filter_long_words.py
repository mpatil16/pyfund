import sys
def filter_long_words():
	word_list = []
	words_count = []
	longest = []
	print("Number of words to enter")
	n = int(sys.stdin.read(1))
	for x in range(n):
		word_list.append(input())
	num = int(input())
	for item in range(n):
		count = 0
		for w in word_list[item]:
			count = count+1
		words_count.append(count)
	for x in range(n):
		if words_count[x]>num:
			longest.append(word_list[x])
	print("List of words longer than number are",longest)


if __name__ == '__main__':
	filter_long_words()
