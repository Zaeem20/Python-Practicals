import re

string = """ 
hey this is durani mohammed zaeem, i am studying in fycs
this is a test string test regex pattern matching...
Ohh i forgot, my age is 17 BTW...
"""

# Matching with finditer in python regex
pattern = re.compile('th')  # checking all `th` occurences

count = 0
for matches in pattern.finditer(string):
    count+=1
    print(f"Match {count} at:",matches.span(), f"Group: {matches.group()}")

print("Coded By Durani Mohammed Zaeem; Roll no: 425")


