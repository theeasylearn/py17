#finally 
try:
    num = int(input("enter num:"))
    answer = num * num *num
    print(answer)

except Exception as e:
    print(e)

finally:
    print("program completed")