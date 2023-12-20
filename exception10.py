# 10000
# 20000

class account():
    balance=10000

    try:
        withdraw=int(input("enter amount of withdrawal:"))
        if withdraw>balance:
            print("your current balance:",balance)
            print("your transection has been cancelled")
            raise Exception("enter valid amount based on you balance")
        
        else:
            balance=balance-withdraw
            print("your final balance",balance)
            print("transection successfully completed")

    except ValueError as v:
        print(v)

    except Exception as e:
        print(e)

    finally:
        if withdraw==10000:
            print("recharge your accout")

        print("have a good day sir")


account()