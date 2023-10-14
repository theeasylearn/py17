#create list 
keys = ['name','age','weight']
person = dict.fromkeys(keys)
print(person)
person['name'] = 'Ankit Patel'
person['age'] = 38
person['weight'] = 85.25
print(person)
#get all values from person 
print(person.values()) #getting all values as list
print(person.keys()) #getting all keys as list
print(person.items()) #getting all key-value pairs as list of tuples
person.pop('age') #remove key-value pair
person.popitem() #remove last key-value pair
print(person)
print(person.get('name')) #get value of key
# person.clear() #clear all key-value pairs