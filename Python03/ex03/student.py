class Person:
	def __init__(self, firstname, lastname) -> None:
		self.firstname = firstname
		self.lastname = lastname

	def __str__(self) -> str:
		return f"{self.firstname} {self.lastname}"

class Student(Person):
	def __init__(self, firstname, lastname, degree=None) -> None:
		super().__init__(firstname, lastname)
		self.degree = degree

	def __str__(self) -> str:
		if (self.degree == None):
			return f"{self.firstname} {self.lastname} is not registered to any course"
		else:
			return f"{self.firstname} {self.lastname} is registered to {self.degree}"
	

if __name__ == "__main__":
	firstname = input("Insert first name: ")
	lastname = input("Insert last name: ")
	is_stud = input("Are you a student? (y/n) ").lower()
	while (True):
		if (is_stud == "y" or is_stud == "n"):
			break
		is_stud = input("Please type \"y\" or \"n\": ")
	if (is_stud == "y"):
		degree = input("Please insert your degree course: ")
		stud = Student(firstname, lastname, degree)
		print(stud)
	else:
		pers = Person(firstname, lastname)
		print(pers)