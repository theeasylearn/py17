#write a program to findout whether given number is prime number or not
number = int(input("Enter number")) #5
diviser = 2
if number % 2 == 0:
    print("Number is not prime")
    exit() # stop the program

while diviser <= (number/2): # 2 < 5
    reminder = number % diviser # 5 % 2 = 1
    if reminder == 0:
        print("Number is not prime")
        #stop this loop 
        break # stop the loop
    else: 
        diviser = diviser + 1 # 3
if diviser == int(number/2) + 1:
    print("Number is prime")
