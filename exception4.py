try:
    user = input("enter file name:")
    file = open(user)
    print(file.read())

except:
    print("wrong input")

else:
    print("file opened successfully")

print("this is some important code")