#write a program to take two number from user and print their sum, subtraction, multiplication, division and floor division result
#input 
#variable = input("message")
num1 = input("enter first number")
num2 = input("enter second number")
#process
num1 = int(num1) #convert string into number 
num2 = int(num2) #convert string into number
#calculate

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
floor = num1 // num2

#output
print("sum is ",sum)
print("subtraction is ",sub)
print("multiplication is ",mul)
print("division is ",div)

