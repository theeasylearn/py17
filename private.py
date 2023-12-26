class myclass:
    def __init__(self):
        self.public = "i am public massage"
        self.__private = "i am private massage"
        
    def display(self):
        print(self.public)
        
    def __p_method(self):
        print(self.__private)
        print("method called")
        
o1 = myclass()
print(o1.public)
# print(o1.__private)
print(o1._myclass__private)

o1._myclass__private = "this is new private"

print(o1._myclass__private)

# o1.private()
# o1._myclass__private()
o1._myclass__p_method()