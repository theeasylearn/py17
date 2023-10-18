#write a program to convert given two digit numbers into words 
#input: 23
#output: two three 
#input: 89
#output: eight nine
words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
number = int(input("Enter number: "))   # 23
first_digit = number // 10  # 2
last_digit = number % 10    # 3
output = words[first_digit] + " " + words[last_digit]
print(output)