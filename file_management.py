# open existing file
file = open("new1.txt","r")
for i in file:
    print(i)

# create new file
file = open("new2.txt","w")

# read method
file = open("new1.txt","r")
print(file.read())
file.close()

# write method
file = open("new1.txt","w")
file.write("this is new data")
file.close()

# append method
file = open("new1.txt","a")
file.write("this is appended data")
file.close()

# mkdir - make directory
import os
os.mkdir("new_dir")

# chdir - change directory
import os
os.chdir("D:\c programming")

# getcwd - current directory
import os
os.getcwd()

# rmdir - remove directory
import os
os.rmdir("new2.txt")