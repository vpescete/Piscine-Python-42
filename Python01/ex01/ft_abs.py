def ft_abs() -> None:
	expr = input("Insert a valid expression: ")
	try:
		res = eval(expr)
		if (res < 0):
			print("The result is: ", str(res * -1))
		else:
			print("The result is: ", str(res))
	except SyntaxError:
		print("Expression is not valid")
	except Exception as e:
		print(f"Error: {e}")

ft_abs()