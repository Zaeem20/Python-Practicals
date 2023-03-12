import re

#write python program using regular expression:
pttrn = r'^h..e$'    # if name string h and endswith e 

strng = input('Enter text: ')
if re.match(pttrn, strng):
    print("Found match")
else:
    print('No match found')

print("Coded By Durani Mohammed Zaeem; Roll no: 425")
