# this is multilevel inheritance
class person:
    def talk(self):
        print("i can talk....")
        
class student(person):
    def read(self):
        print("i can read....")
        
class landuage(student):
    def english(self):
        print("i can speak english....")
        
        
        
# this is single level inheritance
class employee(person):
    def work(self):
        print("i can do work....")
        

# when this two types of inheritance combains , then it will creates hybrid inheritance....