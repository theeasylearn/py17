class person:
    def talk(self):
        print("i can talk....")
        
    def walk(self):
        print("i can walk....")  
        
# o1 = person()
# o1.talk()
# o1.walk()

class student:
    def read(self):
        print("i can read....")
        
    def write(self):
        print("i can write.....")
        
# o2 =student()
        
class landuage(person,student):
    def english(self):
        print("i can speak english....")
        
    def hindi(self):
        print("i can speak hindi....")
        
o3 = landuage()
o3.english()
o3.hindi()

o3.read()
o3.write()

o3.talk()
o3.walk()