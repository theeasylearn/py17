#get date from timstamp 
from datetime import date 
ts = 1397453212
mydate = date.fromtimestamp(ts)
print(mydate)