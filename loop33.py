# write a program to create following pattern 

# * 
# * * 
# * * * 
# * * * * 
# * * * * *
line = 1
while line<=5:
    count = 0
    while count<line:
        print("*",end=' ')
        count = count + 1
    print() #blank line    
    line = line + 1 

