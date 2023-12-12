class Point:
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y
	
	def __str__(self) -> str:
		return f'({self.x}, {self.y})'

class Circle:

	def __init__(self, center, radius) -> None:
		self.radius = radius
		self.center = center

	def __str__(self) -> str:
		return f"Circle with center at {self.center} and radius {self.radius}"

if __name__ == "__main__":
	center_point = Point(150, 100)
	circle = Circle(center_point, 75)
	print(circle)