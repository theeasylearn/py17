try:
    n1 = int(input("enter num 1:"))
    n2 = int(input("enter num 2:"))

    answer = n1/n2
    print(answer)

except ZeroDivisionError :
    print("divide by 0")

except ValueError:
    print("enter proper integer")

else:
    print("division completed")

print("this is imp code")