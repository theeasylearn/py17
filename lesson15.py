#write a program to find sale price of an item from product price + profit percentage. 
#profit percentage is given by user.
#product price is given by user.
price  = int(input("Enter the price of the product: "))
profit = int(input("Enter the profit percentage: "))
profit_amount = price * profit / 100 
#now add profi into price 
# price = price + profit_amount
# or 
price += profit_amount
print("Sale price is: ", price)