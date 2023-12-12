def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9')):
			return False
	return True

def ft_sum() -> None:
	input_one = input("Insert your first integer:")
	input_two = input("Insert your second integer:")
	if (not ft_isdigit(input_one) or not ft_isdigit(input_two)):
		print("You must choose a number")
	else:
		res = int(input_one) + int(input_two);
		print("Result:", res)

ft_sum()