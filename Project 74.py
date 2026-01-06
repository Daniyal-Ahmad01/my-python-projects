class Adder:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return Adder(self.num+other.num)
class Multiplier:
    def __init__(self,num2):
        self.num2=num2
    def __add__(self,other):
        return Adder(self.num2*other.num2)
class SmartCalc(Adder,Multiplier):
    def __init__(self,num3):
        self.num3=num3
    super().Adder()
    super().Multiplier()
a=SmartCalc(4)