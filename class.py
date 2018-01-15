
name = ['Piyush','Abhishek']


class Student:

    def __init__(self,first,last,marks):
        self.first = first
        self.last = last
        self.marks = marks


std_1 = Student(name[0], 'jha', 100)
std_2 = Student(name[1], 'jha', 100)

print(std_2.first)
print(std_1.last)
