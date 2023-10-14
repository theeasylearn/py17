#create set 
fruits = {'apple','orange','banana','apple','orange','banana'}
print(fruits)
set1 = set([1,2,3,4,5,6,7,8,9,10])    
print(set1)
set2 = set([2,4,6,8,10,12,14,16,18,20])
print(set2)
#set union of set1 and set2
newset = set1.union(set2)
print(newset)
#set intersection of set1 and set2
newset = set1.intersection(set2)
print(newset)
#set difference of set1 and set2
newset = set1.difference(set2)
print(newset)