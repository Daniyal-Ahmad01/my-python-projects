# Simple inheritance example demonstrating how classes can extend each other.
# Person is the base class, while Student and Teacher override the info() method
# to add their own fields. This shows basic use of super(), method overriding,
# and code reusability through inheritance.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Name:{self.name}\nAge:{self.age}")
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def info(self):
            super().info()
            print(f"Grade:{self.grade}")
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def info(self):
        super().info()
        print(f"Subject:{self.subject}")
p=Person("Daniyal",17)
s=Student("Ali",16,10)
t=Teacher("Albert",30,"Physics")
p.info()
s.info()
t.info()