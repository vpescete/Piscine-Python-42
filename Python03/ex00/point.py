class Point:

	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y

	def __str__(self) -> str:
		return f'({self.x}, {self.y})'
	
def	ft_sqrt(num, tol=1e-10) -> float:
	guess = num / 2.0
	while (guess**2 - num > tol**2):
		guess = 0.5 * (guess + num / guess)
	return guess

def count_distance(x1, y1, x2, y2) -> None:
	form_quad_dist = f'({x2} - {x1})**2 + (({y2} - {y1})**2)'
	quad_dist = eval(form_quad_dist)
	real_dist = ft_sqrt(quad_dist)
	print(real_dist)

if __name__ == "__main__":
	a = input("Insert the coordinates of the first point: ")
	for i in range(len(a)):
		if a[i] == ',':
			break
	x = a[0:i]
	y = a[i + 1:len(a)]
	point_a = Point(x, y)
	b = Point(input("Insert the coordinates of the second point: "))
	for i in range(len(b)):
		if b[i] == ',':
			break
	x = b[0:i]
	y = b[i + 1:len(b)]
	point_b = Point(x, y)
	count_distance(a.x, a.y, b.x, b.y)