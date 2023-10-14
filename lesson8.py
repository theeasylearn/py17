#create empty dictionary
person = {}
print("dictionary is empty:",person)
#add new key name
person['name'] = 'Ankit Patel'
person['age'] = 38
person['weight'] = 85.25
person['gender'] = True
print(person)
person['subject'] = ['Math','Science','English'] #dictionary has list as value 
person['stages'] = ('child','teen','adult') #dictionary has tuple as value
#update name    
person['name'] = 'Ankit Mahendra Patel'
print(person)