import mysql.connector as con


def InsertData():
    db=con.connect(host="localhost",user="root",passwd="",database='py17',port=3308)
    print("Connection successfull")

    mycursor=db.cursor()

    sql="Insert into products (name,price) values (%s,%s)"

    print("Enter Product Data ")
    name=input("Enter Product Name : ")
    price=int(input("Enter Price of Product "))

    data=[name,price]
    # print(data)

    mycursor.execute(sql,[name,price])
    db.commit()

   


def updateData(id):
    db=con.connect(host="localhost",user="root",passwd="",database='py17',port=3308)
    print("Connection successfull")

    mycursor=db.cursor()

    sql="UPDATE products set name=%s ,price=%s WHERE id =%s "

    print("Update Product Data ")
    name=input("Updade Product Name : ")
    price=int(input("Update Price of Product "))

    data=[name,price,id]
    # print(data)

    mycursor.execute(sql,data)
    db.commit()

def deleteData(id):
    db=con.connect(host="localhost",user="root",passwd="",database='py17',port=3308)
    print("Connection successfull")

    mycursor=db.cursor()

    sql="DELETE FROM products WHERE id=%s "
    data=[id]
    mycursor.execute(sql,data)
    db.commit()

def readData():
    db=con.connect(host="localhost",user="root",passwd="",database='py17',port=3308)
    print("Connection successfull")

    mycursor=db.cursor()

    sql="SELECT * FROM products "
    
    mycursor.execute(sql)

    data=mycursor.fetchall()
    db.commit()
    return data




# rows=InsertData()
# updateData(1)
# deleteData(7) 
# myprodctus =readData()
# print(myprodctus)
# print(f"Total Added Rows :{rows}")
choice=1
while(choice!=5):
    print("Select Any Option  :")
    print("1 for Display product ")
    print("2 for Inser product ")
    print("3 for Update product ")
    print("4 for Delete product ")
    print("5 for Exit ")
    choice=int(input("Enter Your Choice : "))


    if(choice>=1 and choice<=4):

        if(choice==1):
            data=readData()
            for i in data:
                # print(i)
                print("----------------------------------")
                print(f"\tProduct no : {i[0]}")
                print(f"\tProduct name : {i[1]}")
                print(f"\tProduct price : {i[2]}")
                print("----------------------------------")

        elif(choice==2):
            InsertData()
        elif(choice==3):
            id=int(input("Enter The product number you want to Update "))
            updateData(id)
        elif(choice==4):
            id=int(input("Enter The product number you want to Delete "))
            deleteData(id)

        print("Your Opration Completed .................")
        
    else:
        if(choice==5):
            print("Exit .......")
        else:
            choice=5
            print("Invalide Choice .....")                 