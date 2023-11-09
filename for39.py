#example of for loop with tuples
#count odd values and even values
numbers = (10,15,229,11,110,100,3)
odd = 0
even = 0
for num in numbers:
    reminder = num % 2
    if reminder==0:
        even = even + 1
    else:
        odd = odd + 1
print("even count = ",even, " odd count = ",odd)
