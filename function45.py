#example of user defined function 
#def function-name(variable):
#example
#with argument with return value 
def get_square(number):
    #create local variable 
    square = number * number
    return square
def get_qube(number):
    #create local variable
    temp = get_square(number)
    qube = temp * number
    return qube

num = int(input("Enter number to get square"))
#call function 
square = get_square(num)
print(square)

qube = get_qube(num)
print(qube)