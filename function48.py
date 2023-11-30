#example of user defined function with keyword arguments in python 
#create function that total seconds of given hours,minutes, seconds 
def get_seconds(hours,minutes,seconds):
    print(f"hours = $hour, minutes = $minute, seconds = $seconds")
    total_seconds = 0
    total_seconds = (hours * 60 * 60)
    total_seconds += minutes * 60
    total_seconds += seconds
    return total_seconds

h = int(input("Enter hours"))
m = int(input("Enter minutes"))
s = int(input("Enter seconds"))

#call function  using keyword argument concept
total_seconds = get_seconds(seconds=s,hours=h,minutes=m)
print("total seconds = ", total_seconds)


