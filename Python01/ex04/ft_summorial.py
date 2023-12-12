import sys

def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9') and not '.' and not '-'):
			return False
	return True

def ft_summorial() -> None:
	if (len(sys.argv) != 2):
		print("Error! Usage: python3 ft_summorial.py <n>")
		return
	if (not ft_isdigit(sys.argv[1])):
		print("Error! You must pass an integer as argument")
		return
	if (int(sys.argv[1]) <= 0):
		print("Error! n must be >=0")
		return
	num = int(sys.argv[1])
	somma = 0
	for i in range(num + 1):
		somma += i
	print("The sum is:", somma)

ft_summorial()