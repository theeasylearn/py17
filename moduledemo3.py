# import module using sys
import sys 
sys.path.append('H:\\')
import currency_converter
rupees = int(input("Enter rupees"))
dollar = currency_converter.toDollar(rupees)
print(f"dollar = {dollar}")
pound = currency_converter.toPound(rupees)
print(f"pound = {pound}")