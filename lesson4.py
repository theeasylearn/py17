#working with list 
#create list 
menu = ["sabji","roti","dal","rise","sweet","papad","chas"]
stuff = ["ram",True,False,100,12.7]
#display
print(menu)
print(stuff)
print(menu[0]) #print first item in menu 
print(menu[0:2]) #print first 2 items in menu 
print(menu[5:]) #print all items from 5th items onwards
print(menu*2)
print(menu + stuff)
#create empty list
movies = [] #empty list 
print(movies)
menu[0] = "tasty sabji" #replace 0th item in menu 
print(menu)
del menu[3] #remove 3rd item from menu
print(menu)
del stuff #delete whole list 
# print(stuff) #will give error because stuff has been deleted