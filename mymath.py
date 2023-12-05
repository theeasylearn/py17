#example of user defined module 
#module has related functions
def getSquare(number):
    square = number * number 
    return square 
def getQube(number):
    qube = getSquare(number) * number
    return qube
def getAbs(number):
    if number<0:
        number = 0 - number
    return number