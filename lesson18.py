num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#print address of num1 and num2 in memory
print("num1 address: ", id(num1))
print("num2 address: ", id(num2))

result = num1 is num2
print(result)

result = num1 is not num2
print(result)