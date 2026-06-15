class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
    def agep(self):
        print(f"The age of the animal is {self.age}")
d=Animal("Doggesh bhaiya",22)
d.agep()