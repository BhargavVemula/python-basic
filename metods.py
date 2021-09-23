class Student:
    school = 'MGM'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def schlname(cls):
        return cls.school

    @staticmethod
    def info():
        print('this is static method')


s1 = Student(11,22,55)
s2 = Student(35,22,54)
print(s1.avg())
print(s2.avg())
print(s2.get_m1())
s2.set_m1(20)
print(s1.info())
Student.info()

print(Student.schlname())

