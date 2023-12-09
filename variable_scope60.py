#declare global variable
amount = 1000
def AddMoney(rupees):
    global amount
    amount = amount + rupees

rupees = int(input("Enter rupees"))
AddMoney(rupees)
print(f"amount = {amount}")

rupees = int(input("Enter rupees"))
AddMoney(rupees)
print(f"amount = {amount}")