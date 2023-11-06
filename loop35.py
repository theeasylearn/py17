# write a program to create following pattern 

# 1 2 1 2 1
# 1 2 1 2
# 1 2 1
# 1 2 
# 1

line = 5
while line>=1:
    count = 0
    while count<line:
        if(count%2==0):
            print("1",end=' ')
        else:
            print("2",end=' ')
        count = count + 1
    print() #blank line    
    line = line - 1 

