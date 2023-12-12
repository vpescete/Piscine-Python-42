def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9')):
			return False
	return True

def	ft_sum_time() -> None:
	hours = input("Insert hours:")
	minutes = input("Insert minutes:")
	seconds = input("Insert seconds:")
	if (not ft_isdigit(hours) or not ft_isdigit(minutes) or not ft_isdigit(seconds)):
		print("You must insert a number")
	else:
		res = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
		print("Total seconds:", res)

ft_sum_time()