import sys

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
	
	@staticmethod
	def __ft_sqrt(num, tol=1e-10, max_iterations=1000) -> float:
		guess = num / 2.0
		iterations = 0
		while guess**2 - num > tol and guess**2 - num < -tol and iterations < max_iterations:
			guess = 0.5 * (guess + num / guess)
			iterations += 1
		return guess

	def contains(self, point) -> bool:
		distance = self.__ft_sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2)
		return distance <= self.radius

if __name__ == "__main__":
	if (len(sys.argv)) != 3:
		print("Error: too few arguments")
	else:
		point_to_check = Point(float(sys.argv[1]), float(sys.argv[2]))
		circle = Circle(Point(0, 0), 1)

		if circle.contains(point_to_check):
			print(f"The point {point_to_check} lies in the Circle of center (0, 0) and radius 1.")
		else:
			print(f"The point {point_to_check} lies out of the Circle of center (0, 0) and radius 1.")