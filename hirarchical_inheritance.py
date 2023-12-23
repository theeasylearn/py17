class employee:
    def __init__(self,name,age,salary) :
        self.name = name
        self.age = age
        self.salary = salary
        
    def details(self):
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.salary)
        
# o1 = employee("mohanlal",34,10000)
# o1.details()

class programer(employee):
    def __init__(self, name, age, salary,work):
        super().__init__(name, age, salary)
        self.work = work
        
    def p_salary(self):
        print(self.name," is a",self.work)
        print("salary:",self.salary*1.5)
        
o2 = programer("mohanlal",25,10000,"programer")
o2.p_salary()

class ca(employee):
    def __init__(self, name, age, salary,work):
        super().__init__(name, age, salary)
        self.work = work
        
    def ca_salary(self):
        print(self.name,"is a ",self.work)
        print("salary:",self.salary*1.2)
        
o3 = ca("ramesh patel",36,10000,"ca")
o3.ca_salary()