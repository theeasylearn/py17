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
class Actor(Student):
    def Acting(self):
        print("I can do acting...")
    def Dancing(self):
        print("I can do dancing");
    def Fighting(self):
        print("I can do fighting")
    def whatICanDo(self):
        super().eat()
        super().walk()
        super().talk()
        self.Acting()
        self.Dancing()
        self.Fighting()

s1 = Student()
s1.whatICanDo()

a1 = Actor()
a1.whatICanDo()

