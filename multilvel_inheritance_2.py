# write a program that convert gram to kg , kg to tonne , tonne to metric tonne
class kg:
    def __init__(self,gram) :
        self.gram = gram
        
    def getkg(self):
        kg = self.gram / 1000
        print("kg:",kg)
        return kg
    
        
# o1 = kg(3000)
# o1.getkg()

class tonne(kg):
    def __init__(self, gram):
        super().__init__(gram)
        
    def gettonne(self):
        tonne=self.getkg()/1000
        print("tonne:",tonne)
        return tonne
        
# o2 = tonne(4000)
# o2.gettonne()

class metric(tonne):
    def __init__(self, gram):
        super().__init__(gram)
        
    def getmetric(self):
        metric = self.gettonne()/0.907184
        print("metric tonne:",metric)
        
o3 = metric(5000)
o3.getmetric()