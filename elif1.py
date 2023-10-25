#write a program to make addition/subtraction/multiplication/division based upon user on inputed value 
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
choice = int(input("Enter your choice"))
result = 0
if choice<1 or choice>4:
    print("invalid input")
elif choice==1: 
    result = num1 + num2
elif choice==2:
    result = num1 - num2
elif choice==3:
    result = num1 * num2
elif choice==4:
    result = num1 / num2

if choice>=1 and choice<=4:
    print(result)
print("Good bye")