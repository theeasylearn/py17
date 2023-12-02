#write a program to accept 2 person birthdate from user and findout who is younger
from datetime import datetime

#take birthdate as input from user as day, month, year 
print("Enter first person birthdate & time")
day = int(input("Enter day"))
month = int(input("Enter month"))
year = int(input("Enter year"))

hour = int(input("Enter hour"))
minute = int(input("Enter minute"))
seconds = int(input("Enter seconds"))


#create date object 
birth_date_1 = datetime(year,month,day,hour,minute,seconds)

print("Enter second person birthdate & time ")

day = int(input("Enter day"))
month = int(input("Enter month"))
year = int(input("Enter year"))

hour = int(input("Enter hour"))
minute = int(input("Enter minute"))
seconds = int(input("Enter seconds"))

#create date object 
birth_date_2 = datetime(year,month,day,hour,minute,seconds)

print(birth_date_2)

if birth_date_1>birth_date_2:
    print("first person is younger person")
else:
    print("second person is younger person")

print("Good bye..")
