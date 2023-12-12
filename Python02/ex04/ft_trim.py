import sys

def trim(lista) -> None:
	del lista[0]
	del lista[len(lista) - 1]

if __name__ == "__main__":
	if (len(sys.argv)) < 3:
		print("Error! You must insert at least 2 values")
	else:
		lista = []
		for i in range(len(sys.argv) - 1):
			lista.append(sys.argv[i + 1])
		trim(lista)
		print("The new list is:", lista)
	