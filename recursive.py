""" Recursion in Python

Recursion is an approach of which a function call itself, it is used to break problems
in small chunks and solve each chunck one by one. by avoiding iterative programming fashion
sometimes recursive approach have conflict in systems as there is a limit defined in each
system a.k.a MaxRecursionLimit by default it is set to 1000 and can be changed in python.
it is also space consuming approach therefore the space complexity might be higher.
"""

import sys     
sys.setrecursionlimit(10000)  # updating by default recursion limit to avoid RecursionError

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def tower_of_hanoi(ndisk, pole_1, pole_3, pole_2):
    if ndisk == 0:
        # print("Move disk",ndisk,"from source",pole_1,"to destination",pole_3)
        return
    tower_of_hanoi(ndisk-1, pole_1, pole_2, pole_3)
    print("Move disk",ndisk,"from source",pole_1,"to destination",pole_3)
    tower_of_hanoi(ndisk-1, pole_2, pole_3, pole_1)


def print_reverse_using_recursion(n):
    if n > 0:
        print(n)
        print_reverse_using_recursion(n-1)

def print_increment_using_recursion(till, current = 0):
    if current <= till:
        print(current)
        print_increment_using_recursion(till, current+1)

inn = int(input("Enter the Number: "))
print(f"Factorial of {inn}:", factorial(inn))   
print(f'Fibonacci Series of {inn}:', fibonacci(inn))

print()
print()
print("Tower of Hanoi using Recursion: ")
tower_of_hanoi(3, 'PL-A', 'Pl-B', 'PL-C')
print()
print("printing in reverse order using recursion")
print_reverse_using_recursion(10)
print()
print("Printing until n using recursion")
print_increment_using_recursion(10)

print("Coded by Durani mohammed zaeem: Roll no: 425")