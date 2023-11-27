#write a program to findout all the even number between given range using for loop 
start = int(input("Enter start number")) # 10
stop = int(input("Enter second number")) # 100
stop = stop + 1
for num in range(start,stop):
    reminder = num % 2 #0
    if reminder == 0:
        print(num,end=' ')
