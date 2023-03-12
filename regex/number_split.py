import re

# splitting texts with number using python regex
num = r'\d+'

inp = input("Enter String:")
rslt = re.split(num, inp)
print("string without numbers", rslt)

print("Coded By Durani Mohammed Zaeem; Roll no: 425")
