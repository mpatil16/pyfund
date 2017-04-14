import sys
def word_count():
	word_list = []
	words_count = []
	print("Number of words to enter")
	n = int(sys.stdin.read(1))
	for x in range(n):
		word_list.append(input())
	for item in range(n):
		count = 0
		for w in word_list[item]:
			count = count+1
		words_count.append(count)
	print("Word count of each word is",words_count)


if __name__ == '__main__':
	word_count()
