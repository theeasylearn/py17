#example of user defined function in python 
#create function that total seconds of given hours,minutes, seconds 
def get_seconds(hours,minutes=0,seconds=0):
    total_seconds = 0
    total_seconds = (hours * 60 * 60)
    total_seconds += minutes * 60
    total_seconds += seconds
    return total_seconds

hours = int(input("Enter hours"))
minutes = int(input("Enter minutes"))
seconds = int(input("Enter seconds"))

#call function 
total_seconds = get_seconds(hours,minutes,seconds)
print("total seconds = ", total_seconds)

total_seconds = get_seconds(hours,minutes)
print("total seconds = ", total_seconds)

total_seconds = get_seconds(hours)
print("total seconds = ", total_seconds)

