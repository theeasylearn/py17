#write a program to accept selling price and production price from user. findout profit or loss amount
#input
selling_price = int(input("Enter selling price: "))
production_price = int(input("Enter production price: "))
#process
profit_loss = selling_price - production_price
if profit_loss > 0:
    print("Profit amount is: ",profit_loss)
else:    
    print("Loss amount is: ",profit_loss)   

print("Thank you")