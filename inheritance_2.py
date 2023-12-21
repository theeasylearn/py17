class Person:
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")
class Student(Person):
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def whatICanDo(self):
        #calling parent class function
        super().walk()
        super().talk()
        super().eat()
        #calling same class 
        self.read()
        self.write()
class Developer(Student): 
    def code(self):
        print("I can write code")
    def debug(self):
        print("I can debug code")
    def whatICanDo(self):
        super().whatICanDo()
        self.code()
        self.debug()
 
#create Developer class object
d1 = Developer()
d1.whatICanDo() #this will call child class method because d1 is object of child class 
