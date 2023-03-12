# Program to find minimum and maximum in a list using Python.

lis = list(map(int, input("Enter numbers seperated with `,`: ").split(',')))

# There are n numbers of approach to do this task, we also have builtin min() and max() in python
# to get maximum and minimum from list, we have to sort it in ascending order.
# here i am using built in sorted() function in python.
new_list = sorted(lis)

print("Maximum in a List:", new_list[-1])  # last number will be maximum
print("Minimum in a List:", new_list[0])   # first number will be minimum

print("Coded by Safdar Queshi asgar ali: Roll no: 454")

print()


#Program to sum of all element in array.
my_list=[45,65,89,78,35]
print("Sum of Items:",sum(my_list))

print()

# Program to count odd and even numbers in list using Python  
# We will perform bitwise operation on a number to check whether number is odd or even.

lis = list(map(int, input("Enter numbers seperated with commas `,`: ").split(',')))

TotalEven=0
TotalOdd=0

for i in lis:
    if not i&1:
        TotalEven+=1
    else:
        TotalOdd+=1
print("Total Odd numbers: ", TotalOdd)
print("Total Even numbers: ", TotalEven)


print()
print()

import numpy
print(numpy.fromiter("Hi this is Safdar Qureshi Asgar ali", "U2"))
