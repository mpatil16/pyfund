import sys

vowels = ['a','e','i','o','u']


def vowel_with_for(character):
	"""This method is to check whether particular character is Vowel or not
		
	
	
	"""
	if character in vowels:
		print("Entered character is vowel..!")
	else:
		print("Not a Vowel")

		
if __name__ == '__main__':
	#vowel(sys.stdin.read(1))
	vowel_with_for(sys.stdin.read(1))