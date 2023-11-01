#write a program to print following pattern 
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 10 = 50
count = 1
num = 5

while count<=10:
    result = num * count;
    print("5 x ",count," = ",result)
    count = count + 1


