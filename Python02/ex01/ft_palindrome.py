import sys

def is_palindrome(stringa):
	begin = 0
	end = len(stringa) - 1
	while (begin < (len(stringa) / 2)):
		if (stringa[begin] != stringa[end]):
			print("The string", stringa, "is not palindrome")
			return False
		begin += 1
		end -= 1
	return True

def ft_palindrome():
	if (len(sys.argv) == 1 or len(sys.argv) > 2):
		print("Error! Insert just 1 string!")
		return False
	boolean = is_palindrome(sys.argv[1])
	if (boolean == True):
		print("The string", sys.argv[1], "is palindrome")
	elif (bool == False):
		print("The string", sys.argv[1], "is not palindrome")

ft_palindrome()