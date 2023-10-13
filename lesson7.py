#create dictionary  
person = {'name':'Ankit Patel','age':38,'weight':85.25,'gender':True}
print(person)
#update name    
person['name'] = 'Ankit Mahendra Patel'
print(person['name'])
#add new key email  
person['email'] = 'ankit@gmail.com'
print(person)
#delete key email
del person['email']
print(person)
