try:
    num = int(input("enter num:\n"))
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

except Exception :
    print("enter number")

else:
    print("task comleted")

print("some imp code")