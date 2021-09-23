class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.config = 'i5'

        def show(self):
            print(self.brand, self.config)


s1 = Student('bhargav', 101)
s2 = Student('kalpana', 102)

lap1 = Student.Laptop()
lap2 = Student.Laptop()

print(lap1.brand)
print(lap1.show())


