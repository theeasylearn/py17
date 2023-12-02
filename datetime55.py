from datetime import time 

hour = int(input("Enter hour"))
minute = int(input("Enter minute"))
seconds = int(input("Enter seconds"))

#create time object 
time1 = time(hour,minute,seconds)

hour = int(input("Enter hour"))
minute = int(input("Enter minute"))
seconds = int(input("Enter seconds"))

#create time object 
time2 = time(hour,minute,seconds)
print(time1)
print(time2)

if time1<time2:
    print("first time is smaller then second time")
else:
    print("second time is smaller then first time")
