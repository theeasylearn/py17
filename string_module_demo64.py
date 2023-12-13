line = input("enter input")
print(line)

#print input in lowercase
print(line.lower())

#print input in uppercase
print(line.upper())

#check input has only alphabets or not 
if line.isalpha()==True:
    print("input has only alphabets")
else:
    print("input has alphabets and other letters")

if line.islower()==True:
    print("input has only lowercase letters")
else:
    print("input has differnt  case letters")


if line.isupper()==True:
    print("input has only uppercase letters")
else:
    print("input has differnt case letters")

if line.istitle()==True:
    print("input is in title case")
else:
    print("input is not in title case")

if line.isdigit()==True:
    print("input has digits")
else:
    print("input has digits and other symbols")