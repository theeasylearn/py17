# 5
# 1*2*3*4*5

try:
    num = int(input("enter num:"))
    ans=1
    for i in range(1,num+1):
        ans=i*ans
    print(ans)

except ValueError:
    print("enter integer")

finally:
    print("this is some important code")