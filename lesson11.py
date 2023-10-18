#write a program to convert given minutes into hours and minutes 
#input: 100
#output: 1 hour 40 minutes
#input: 200     
#output: 3 hours 20 minutes
minutes = int(input("Enter minutes: "))
# minutes = int(minutes) 
hours = minutes // 60 
remaining_minutes = minutes - (hours * 60)
print(hours," hours",remaining_minutes," minutes")