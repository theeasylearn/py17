line = input("Enter any one line text")
print(line)
#count how many letters including space line has (length)
length = len(line)
print(length)

list = ['apple','banana','mango','pinapple','graps']
print(list)
#store all items of list as string
connector = "-"
fruits = connector.join(list)
print(fruits)

old_word = "india"
new_word = "bharat"

print(line.replace(old_word,new_word))
