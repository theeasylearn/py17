# write a program to create following pattern 

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
line = 0
while line<=4:
    count = 0
    while count<=4:
        print("*",end=' ')
        count = count + 1
    print() #blank line    
    line = line + 1 

