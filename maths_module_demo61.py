import math  
number = float(input("Enter number"))
print(number)
big_value = math.ceil(number)
small_value = math.floor(number)
truncated_value = math.trunc(number)
print(f"big value = {big_value} small value = {small_value} truncated value = {truncated_value}")