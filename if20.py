#write a program to findout whether given number is even or odd
#input
number = int(input("Enter a number to findout whether it is odd or even: ")) # 11
#process    
reminder = number % 2
if reminder == 0: # < > <= >= == !=
    print(number, " is even number")
else:
    print(number, " is odd number")
#output
print("Good bye")