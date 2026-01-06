# This class demonstrates the use of __repr__ and __str__ methods in Python.
# __repr__ returns an official, unambiguous string useful for debugging.
# __str__ returns a user-friendly string for display purposes.
class Student:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f"Student(name='{self.name}')"
    def __str__(self):
        return f"Student name is {self.name}"
a=Student("Daniyal")
print(repr(a))
print(str(a))
print(a)