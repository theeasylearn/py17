# //write a program calculate qube of given positive number 
number = int(input("Enter a positive number: "))
if number<0: # < > <= >= == !=
    print("it is negative number so let us convert it to positive")
    number = -number
    
qube = number * number * number
print("Qube of", number, " is ", qube)