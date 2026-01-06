# This class includes a classmethod constructor (from_separate) that
# allows creating a Student object from a single 'name-grade' formatted string.
# Useful for parsing input data while keeping object creation clean and readable.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def from_separate(cls, string):
        name, grade = string.split("-")
        return cls(name, grade)
