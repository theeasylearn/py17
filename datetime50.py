import datetime 

#get currentdate and time 
CurrentDateTime = datetime.datetime.now()
print("Current Date & Time ",CurrentDateTime)

#get current date 
CurrentDate = datetime.date.today()
print("Current Date ",CurrentDate)

#store & display date in indian format
#dd-mm-yyyy
mydate = str(CurrentDate.day) + "-" + str(CurrentDate.month) + "-" + str(CurrentDate.year)
print(mydate)