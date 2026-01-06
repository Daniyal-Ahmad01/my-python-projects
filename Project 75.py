class Academics:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
class Sports:
    def __init__(self,sportname,score):
        self.sportname=sportname
        self.score=score
class Student(Academics,Sports):
    def __init__(self,name,marks,sportsname,score):
        Academics.__init__(self,name,marks)
        Sports.__init__(self,sportsname,score)
    def detail(self):
        print(f"Name :\t{self.name}\nMarks:\t{self.marks}\nSportsname:\t{self.sportname}\nScore:\t{self.score}")
a=Student("Daniyal",67,"Football",10)
a.detail()