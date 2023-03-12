import re

# Name validation program using regex in python
def validate_input(string):
    not_allowed= re.compile('[@#$%^&*()<>~]')
    if not_allowed.search(string):
        print("String cannot contain special symbols")
    else:
        print('Thanks for submitting')

inputs = input('Enter text: ')
validate_input(inputs)

print("Coded By Durani Mohammed Zaeem; Roll no: 425")