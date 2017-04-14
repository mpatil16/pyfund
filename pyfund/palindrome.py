def palindrome(str1):
	str1 =str1
	l=[]
	for x in str1:
		l.append(x)
	l.reverse()
	str2 = ''.join(l)
	if str1 == str2:
		print("String entered is palindrome!")
	else:
		print("Not a Palindrome!")

if __name__ == '__main__':
	palindrome(input())
