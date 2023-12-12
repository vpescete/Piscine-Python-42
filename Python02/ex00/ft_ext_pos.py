import sys

def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9') and not '.' and not "-"):
			return False
	return True

def ft_max(lista) -> None:
	xmax = lista[0]
	pos = 0
	for i in lista:
		if xmax < i:
			xmax = i
	for i in range(len(lista)):
		if xmax == lista[i]:
			pos = i
	print("The max is,", xmax," and its position is", pos)

def ft_min(lista) -> None:
	xmin = lista[0]
	pos = 0
	for i in lista:
		if xmin > i:
			xmin = i
	for i in range(len(lista)):
		if xmin == lista[i]:
			pos = i
	print("The min is,", xmin," and its position is", pos)

def ft_ext_pos() -> None:
	if (len(sys.argv) == 1):
		print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
		return
	i = 0
	lista = []
	while (i < len(sys.argv) - 1):
		if (not ft_isdigit(sys.argv[i + 1])):
			print("Error! You must pass integer as argumets")
			return
		lista.append(int(sys.argv[i + 1]))
		i += 1
	ft_min(lista)
	ft_max(lista)

ft_ext_pos()