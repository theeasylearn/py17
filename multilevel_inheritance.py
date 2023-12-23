# bytes >> kb >> mb >>gb
class kb:
    def __init__(self,bytes):
        self.bytes = bytes
        
    def getkb(self):
        kb = self.bytes / 1024
        print("kb:",kb)
        
# o1 = kb(2048)
# o1.getkb()

class mb(kb):
    def __init__(self, bytes):
        super().__init__(bytes)
        
    def getmb(self):
        mb = self.bytes / (1024*1024)
        print("mb:",mb)
        
# o2 = mb(1024)
# o2.getmb()

class gb(mb):
    def __init__(self, bytes):
        super().__init__(bytes)
        
    def getgb(self):
        gb = self.bytes / (1024*1024*1024)
        print("gb:",gb)
        
        
user = int(input("enter bytes:"))
o3 = gb(user)
o3.getkb()
o3.getmb()
o3.getgb()