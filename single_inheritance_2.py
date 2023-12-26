# write a program that convert gram to kg , kg to tonne
class kg:
    def __init__(self,gram):
        self.gram = gram
        
    def getkg(self):
        kg= self.gram/1000
        print("kg:",kg)
        return kg
        
# o1 = kg(2000)
# o1.getkg()

class tonne(kg):
    def __init__(self, gram):
        super().__init__(gram)
        
    def gettonne(self):
        tonne=self.getkg()/1000
        print("tonne:",tonne)
        
o2 = tonne(2000)
# o2.getkg()
o2.gettonne()