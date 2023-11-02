# write a program to findout whether given number is palindrom number or not 
# #input = 121
# #reverse = 121
# if inputed number is same as reverse number then it is paliendrom  otherwise not palindrom 
number = int(input("Enter number")) #123
reverse = 0
while  number>0:
    last_digit = number % 10
    reverse = (reverse * 10) + last_digit #3
    number = number // 10 #12
print(reverse)


