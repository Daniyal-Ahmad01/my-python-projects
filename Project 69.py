# Person Class with Classmethod Constructor
# -----------------------------------------
# This script demonstrates how to use a classmethod as an alternative
# constructor. The `from_birth` method creates a Person instance by 
# calculating age from a given birth year. It showcases clean object 
# initialization and a beginner-friendly example of classmethod usage.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_birth(cls,name,b):
        age=2025-int(b)
        return cls(name,age)
a=Person.from_birth("Daniyal","2009")
print(a.age)