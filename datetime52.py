#write a program to accept 2 person birthdate from user and findout who is younger
import datetime 

#take birthdate as input from user as day, month, year 
print("Enter first person birthdate detail")
day = int(input("Enter day"))
month = int(input("Enter month"))
year = int(input("Enter year"))

#create date object 
birth_date_1 = datetime.date(year,month,day)

print("Enter second person birthdate detail")

day = int(input("Enter day"))
month = int(input("Enter month"))
year = int(input("Enter year"))

#create date object 
birth_date_2 = datetime.date(year,month,day)

print(birth_date_2)

if birth_date_1>birth_date_2:
    print("first person is younger person")
else:
    print("second person is younger person")

print("Good bye..")
