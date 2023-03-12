from datetime import datetime
birthday = datetime(*list(map(int, input("Enter your Birthdate in YYYY/MM/DD: ").split('/'))))
print(f'Days Passed from Birthdate: {datetime.now().date() - birthday.date()} ago')

print("Coded By Durani Mohammed Zaeem Abdul Qadir: Roll no:- 425")
