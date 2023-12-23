# byte >> kb >> mb
class kb:
    def __init__(self,bytes):
        self.bytes = bytes
        
    def getkb(self):
        kb = self.bytes /1024
        print("kb:",kb)
        
# o1 = kb(2048)
# o1.getkb()

class mb(kb):
    def __init__(self, bytes):
        super().__init__(bytes)
        
    def getmb(self):
        mb = self.bytes / (1024*1024)
        print("mb:",mb)

o2 = mb(2048)
o2.getkb()
o2.getmb()