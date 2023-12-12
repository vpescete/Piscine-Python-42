import sys

def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9')):
			return False
	return True

def	ft_sum_row(lista) -> list:
	somma = []
	for i in lista:
		temp = 0
		for j in i:
			temp += j
		somma.append(float(temp))
	return (somma)

def	ft_sum_col(lista) -> list:
	somma = []

	for i in range(len(lista[0])):
		temp = 0
		for j in range(len(lista)):
			temp += lista[j][i]
		somma.append(float(temp))
	print(somma)
	return (somma)

def ft_matrix() -> None:
	if (len(sys.argv) != 3):
		print("Error! Usage: python3 ft_matrix.py <n> <m>")
		return
	if (not ft_isdigit(sys.argv[1] or not ft_isdigit(sys.argv[2]))):
		print("Error! Usage: python3 ft_matrix.py <n> <m>")
		return
	rows = int(sys.argv[1])
	columns = int(sys.argv[2])
	lista = []
	y = 0
	print(rows)
	while y < rows:
		row = []
		x = 0
		while x < columns:
			num = input("Insert the element in position ({}, {}): ".format(y, x))
			row.append(float(num))
			x += 1
		
		lista.append(row)
		y += 1
	print("The inserted matrix is:")
	for i in lista:
		print(i)
	sum_row = ft_sum_row(lista)
	sum_col = ft_sum_col(lista)
	print("The sum over rows is:")
	print(sum_row)
	print("The sum over columns is:")
	print(sum_col)


ft_matrix()