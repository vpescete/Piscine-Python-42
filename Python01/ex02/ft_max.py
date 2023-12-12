import sys

def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9') and not '.' and not '-'):
			return False
	return True

def ft_max() -> None:
	if (len(sys.argv) != 4):
		print("Error! Usage: python3 ft_max.py <x> <y> <z>")
		return
	if (not(ft_isdigit(sys.argv[1])) or not(ft_isdigit(sys.argv[2])) or not(ft_isdigit(sys.argv[3]))):
		print("Error: You must pass numbers or float as arguments")
	one = float(sys.argv[1])
	two = float(sys.argv[2])
	tree = float(sys.argv[3])
	lista = [one, two, tree]
	xmax = lista[0]
	for i in lista:
		if xmax < i:
			xmax = i
	print("The max is:", xmax)

ft_max()
