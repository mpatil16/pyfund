import sys
def longest_word():
	word_list = []
	words_count = []
	longest = 0
	print("Number of words to enter")
	n = int(sys.stdin.read(1))
	for x in range(n):
		word_list.append(input())
	for item in range(n):
		count = 0
		for w in word_list[item]:
			count = count+1
		words_count.append(count)
	for x in range(n):
		if longest<words_count[x]:
			longest = words_count[x]
	print("Length of longest word is",longest)


if __name__ == '__main__':
	longest_word()
