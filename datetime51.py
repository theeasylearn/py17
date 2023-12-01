import datetime 

#take birthdate as input from user as day, month, year 

day = int(input("Enter day"))
month = int(input("Enter month"))
year = int(input("Enter year"))

#create date object 
birth_date = datetime.date(year,month,day)
print(birth_date)