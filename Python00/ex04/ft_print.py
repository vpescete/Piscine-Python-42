def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9')):
			return False
	return True

def ft_print() -> None:
	string = input("Insert a string: ")
	pos = int(input("Insert an integer: "))
	if (len(string) < pos):
		print("Error: index out of range")
		return
	elif (not ft_isdigit(str(pos))):
		print("Choose an integer")
		return
	print(string[pos: len(string) - pos + 1])

ft_print()