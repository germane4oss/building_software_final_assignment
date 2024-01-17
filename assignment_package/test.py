class Student:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

std = Student('Bill',25) #passing values to constructor
print(std.name)
print(std.age)