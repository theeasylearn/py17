fruits = ['apple', 'banana', 'cherry']
vegitables = ('carrot', 'lettuce', 'onion')
animals = {'dog', 'cat', 'bird'}

fruit = input("Enter a fruit: ")
print(fruit)
result = fruit in fruits
print(result)

veg = input("Enter a vegitable: ")
result = veg in vegitables
print(result)

animal = input("Enter an animal: ")
result = animal in animals
print(result)

fruit = input("Enter a fruit: ")
print(fruit)
result = fruit not in fruits
print(result)

veg = input("Enter a vegitable: ")
result = veg not in vegitables
print(result)

animal = input("Enter an animal: ")
result = animal not in animals
print(result)