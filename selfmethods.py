
class Student:
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

	def details(self):
		print("{} student marks are {}".format(self.name, self.marks))


s1 = Student("bhargav",95)
s1.details()
