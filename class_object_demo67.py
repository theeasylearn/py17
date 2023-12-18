#create class 
class Student:
    #class variable
    InsituteName = "the easylearn academy"
    def __init__(self,rollno,name,gender):
        self.rollno = rollno
        self.name = name
        self.gender = gender
    def display(self):
        print(self.rollno)
        print(self.name)
        print(self.gender)

#create object
s1 = Student(1000,"Vishva Viradiya",False)
s2 = Student(1001,"Bhutik makwana",True)
s1.display()
s2.display()
print(Student.InsituteName)
print(s1.InsituteName)
print(s2.InsituteName)
Student.InsituteName = "T.E.L";
print(Student.InsituteName)
print(s1.InsituteName)
print(s2.InsituteName)

