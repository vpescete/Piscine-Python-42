import sys

def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9') and not '.' and not "-"):
			return False
	return True

def ft_compare() -> None:
	if len(sys.argv) != 3:
		print("Error: You must pass 2 argumets!")
		return
	if (not ft_isdigit(sys.argv[1]) or not ft_isdigit(sys.argv[2])):
		print("Error: Argument must be interger or float")
		return
	num_one = float(sys.argv[1])
	num_two = float(sys.argv[2])
	if (num_one > num_two):
		print(num_one, " is greater than ", num_two)
	elif (num_one == num_two):
		print(num_one, " is equal to ", num_two)
	elif (num_one < num_two):
		print(num_one, " is less than ", num_two)

ft_compare()