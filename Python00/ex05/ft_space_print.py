def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9')):
			return False
	return True

def ft_space_print() -> None:
	string = input("Insert a string: ")
	start = 0
	if len(string) > 20:
		start = len(string) - 20
		print(string[start:])
	else:
		space = " " * (19 - len(string))
		print(space, string[start:])

ft_space_print()