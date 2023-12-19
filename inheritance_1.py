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

#create parent class object
p1 = Person()
p1.eat()
p1.talk()
p1.walk()

#child class object 
s1 = Student()
s1.whatICanDo()
#calling parent class function using child class object 
s1.walk()
s1.write()
