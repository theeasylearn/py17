class multiplication:
    def area(self,a=None,b=None):
        if a!=None and b!=None:
            print(a*b)

        elif a!=None:
            print(a*a)

        else:
            print("nothing inserted")
            
# o1 = multiplication()
# o1.area(2)

o1 = multiplication()
o1.area(2,5)
o1.area(3)
o1.area()