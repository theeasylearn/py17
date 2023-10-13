#how to create tuple 
gods = ('Bramha','Shiv','Vishnu','Shiv')
print(gods)
#print first element of tuple
print(gods[0])
#print 2nd element of tuple
print(gods[1])
#print 3rd element of tuple
print(gods[2])
#print 1st 2 elements of tuple  
print(gods[0:2])
#print last 2 elements of tuple 
print(gods[1:])
# gods[0] = 'Bramha Bhagwan' #error   
print(gods)
#find whether tuple has element or not
position = gods.index('Vishnu')
print(position)
#count how many shiv are there in tuple 
count = gods.count('Shiv')
print(count)
print(gods * 5)
