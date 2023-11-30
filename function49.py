#function that returns multiple value 
#create function that converts and return rupees into dollar,pound & yen 
def convert(rupees):
    dollar = rupees * 0.012
    pound = rupees * 0.0094
    yen = rupees * 1.76
    return dollar,pound,yen

rs = int(input("Enter rupees"))
currencies = convert(rupees=rs)
print(currencies)