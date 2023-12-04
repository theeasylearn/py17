#convert specific date into various format like indian format, us format 
'''
%m: Month as a zero-padded decimal number (01, 02, ..., 12).
%B: Full month name (e.g., January).
%b: Abbreviated month name (e.g., Jan).
%d: Day of the month as a zero-padded decimal number (01, 02, ..., 31).
%A: Full weekday name (e.g., Monday).
%a: Abbreviated weekday name (e.g., Mon).
%H: Hour (00, 01, ..., 23).
%I: Hour (01, 02, ..., 12).
%p: AM or PM.
%M: Minute as a zero-padded decimal number (00, 01, ..., 59).
%S: Second as a zero-padded decimal number (00, 01, ..., 59).
'''
from datetime import datetime
birth_date = input("give your birthdate in dd-mm-yyyy format")
print(birth_date)

us_format_date = datetime.strptime(birth_date,'%d-%m-%Y')
print(us_format_date.strftime('%A %m-%d-%Y'))