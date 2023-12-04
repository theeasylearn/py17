#convert current date into various format like indian format, us format 
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

#get current date time 
now = datetime.now(); 
print("Current date time",now)

#convert date into indian format 
indian_format_date = now.strftime('%d-%m-%Y')
print(indian_format_date)

us_format_date = now.strftime("%m-%d-%Y")
print(us_format_date)
# Monday 04-January-2023 
custom_format =  now.strftime("%A %d-%B-%Y")
print(custom_format)
