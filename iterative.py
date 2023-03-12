def print_in_reverse(n):
    for i in range(n, 0, -1):
        print(i)

def print_in_sequence(n):
    for i in range(0, n):
        print(i)

print("Iterative Approach for printing reverse")
print_in_reverse(5)
print("Iterative Approach for printing sequence")
print_in_sequence(5)