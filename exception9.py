try:
    age = int(input("enter your age:"))
    
    if age>=18:
        print("eligible for voting")

    else:
        if age<0:
            raise Exception("negetive number")
        else:
            print("invlid input")

except Exception as e:
    print(e)