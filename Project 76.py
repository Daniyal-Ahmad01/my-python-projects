class Employee:
    def __init__(self,name,ID,dept):
        self.name=name
        self.ID=ID
        self.dept=dept
class FullTimeEmployee(Employee):
    def __init__(self,name,ID,dept,salary):
        super().__init__(name,ID,dept)
        self.salary=salary
class Manager(FullTimeEmployee):
    def __init__(self,name,ID,dept,salary,bonus):
        super().__init__(name,ID,dept,salary)
        self.bonus=bonus
    def info(self):
        print(f"Name:\t{self.name}\nID:\t{self.ID}\nDepartment\t{self.dept}\nSalary:\t{self.salary}\nBonus:\t{self.bonus}")
a=Manager("Daniyal",1401,"Dept",1400,100)
a.info()