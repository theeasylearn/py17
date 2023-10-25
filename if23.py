# write a program to findout shortest person from 3 person 
height1 = int(input("Enter 1st person height"))
height2 = int(input("Second person height"))
height3 = int(input("Enter 3rd person height"))

if height1<height2: #== < > != >= <=
    if height1<height3:
       print("1st person is shortest person") 
    else:
       print("3rd person shortest person")
else:
   if height2<height3:
      print("2nd person is shortest person")
   else:
      print("3rd person is shortest person")
print("good bye")