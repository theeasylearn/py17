try:
    list = ["python","c++","java","html"]
    print(list)

    num = int(input("entter number:"))
    print(list[num])

except(ValueError,IndexError):
    print("wrong input")

print("this is some important code")