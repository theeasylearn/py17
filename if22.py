# //write a program to accept month number from user and display number of days in that month
# 1, 3, 5, 7, 8, 10, 12 = 31
# 4, 6, 9, 11 = 30
# 2 = 28/29o
#input:
month = int(input("Enter month number: "))  
#process:
if month<1 or month>13:
    print("this is invalid month")
else:
    if month == 1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print("this month has 31 days ")

    if month==4 or month==6 or month==9 or month==11:
        print("this month has 30 days")

    if month==2:
        print("this month has 28/29 days")
    
print("good bye....")