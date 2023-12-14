import string
import random
def GeneratePassword(length=12):
    #store all alphabets in lowercase, uppercase and digits into variable line
    line =  string.ascii_lowercase + string.ascii_uppercase + string.digits
    seeds = list(line)
    random.shuffle(seeds)
    password = ''.join(seeds)[0:length]
    return password
password = GeneratePassword(20)
print(password)