import sys

def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9')):
			return False
	return True

def sum_list(lista) -> int:
	somma = 0
	for i in lista:
		somma = somma + i
	return somma

def ft_sum_list() -> None:
	lista = []
	while (True):
		num = input("Insert an integer:")
		if (not ft_isdigit(num)):
			print("Error: You must insert integer")
			return
		if (int(num) == 0):
			break
		lista.append(int(num))
	print("The sum is:", sum_list(lista))

ft_sum_list()