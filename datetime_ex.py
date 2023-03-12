from datetime import datetime, date

dates = date(2005, 2, 24)
print("Date was:", dates, end='\n\n')

today = datetime.now()    # Creating Object for current Date

# Today's current Date.
print(f'Today\'s Date is: {today}')

# Getting Year, month, day:
print('\n\nToday\'s Date Summary')
print(f"""Year: \033[1;92m{today.year}\033[0m
Month : \033[1;92m{today.month}\033[0m
Day: \033[1;92m{today.day}\033[0m""")

# Getting Date from timestamp:
print(f"\n\nGetting Date from Timestamp: {datetime.fromtimestamp(784543546)}")

# Getting hour, minutes, seconds, microseconds:
print(f"\nToday's time summary:\n\
Hour: {today.hour}\n\
Minutes: {today.minute}\n\
Seconds: {today.second}\n\
Microsec: {today.microsecond}\n")

# Getting current date and time (well-formated):
print(f'Current Date: {today.strftime("%d-%b-%Y")}\n\
Current Time: {today.strftime("%X")}')

print("\nCoded By Durani Mohammed Zaeem: Roll No:- 425")