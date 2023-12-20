try:
    num1 = int(input("enter number1:"))
    num2 = int(input("enter number2:"))

    print("1 for add")
    print("2 for sub")
    print("3 for mul")
    print("4 for div")

    choise = int(input("enter choise:"))

    if choise==1:
        print(num1+num2)

    elif choise==2:
        print(num1-num2)

    elif choise==3:
        print(num1*num2)

    elif choise==4:
        print(num1/num2)

except Exception as e:
    print(e)

else:
    print("task complted")

finally:
    print("program completed")