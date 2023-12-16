#create class 
class Product:
    def __init__(self,name,price,weight): #constructor
        # //instance variables 
        self.name = name
        self.price = price
        self.weight = weight
        print("constructor called....")
    def calculatePricePerWeight(self):
        self.price_per_gram = self.price / self.weight
    def display(self):
        self.calculatePricePerWeight();
        print("Product Name " + self.name)
        print("Price " + str(self.price))
        print("Weight " + str(self.weight))
        print("Price per gram " + str(self.price_per_gram))
    def setPrice(self,price):
        self.price = price 
    def setWeight(self,weight):
        self.weight = weight
#create object of product class 
name = input("Enter product name")
price = int(input("Enter price"))
weight = float(input("Enter weight"))

p1 = Product(name,price,weight)
p1.display()
price = int(input("Enter new product price"))
p1.setPrice(price)
weight = float(input("Enter new product weight"))
p1.setWeight(weight)
p1.display()
