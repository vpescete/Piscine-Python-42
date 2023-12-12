import sys

def ft_isdigit(n) -> bool:
	for i in n:
		if (not('0' <= i <= '9') and not '-'):
			return False
	return True

def insertion_sort(lista) -> list:
	for i in range(1, len(lista)):
		key = lista[i]
		j = i - 1
		while j >= 0 and key < lista[j]:
			lista[j + 1] = lista[j]
			j -= 1
		lista[j + 1] = key
	return lista

def ft_sorted() -> None:
	if len(sys.argv) <= 2:
		print("Error! You must insert at least 2 numbers")
		return
	sort = True
	lista = []
	for i in range(len(sys.argv) - 1):
		if (not ft_isdigit(sys.argv[i + 1])):
			print("Error! You must pass integers as arguments")
			return
		lista.append(int(sys.argv[i + 1]))
	for i in range(len(lista)):
		if lista[i] <= lista[i + 1]:
			sort = False
			break
	if (sort == True):
		print("The inserted sequence is sorted!")
		return
	else:
		print("The inserted sequence is not sorted!")
	lista = insertion_sort(lista)
	print("The correct order is", lista)
	


ft_sorted()