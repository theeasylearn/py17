#withtout argument without return value function
def PrintLine():
    print("-" * 100)

#with argument without return value function
def PrintLetter(letter,repeat_count):
    print(letter * repeat_count)

#without argument with return value 
def get_pi():
    pi = 3.141516
    return pi

PrintLetter('*',200)
PrintLine()
PrintLetter('$',150)
pi = get_pi()
print("pi = ",pi)