#write a program to make sum of all digits of given number 
#input = 12345
# process = 1+2+3+4+5
#output = 15
number = int(input("Enter number")) #123
sum = 0
while number>0:
    last_digit = number % 10 
    sum = sum + last_digit
    number = number // 10
print(sum)
