#write a program to print following pattern
'''
123456789
123456789
123456789
123456789
123456789
'''
count = 0
while count < 5: # outer loop 
    number = 0 
    while number<9: # inner loop 
        number = number + 1
        print(number,end=" ")
    print() # new line
    count = count + 1
