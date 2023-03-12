import numpy as np
from tabulate import tabulate

x = [[12,7,9],[8,9,7],[7,8,6]]
y = [[2,8,8],[1,9,8],[7,5,6]]

result = np.zeros((3,3))
# addition of matrix
for i in range(len(x[0])):
    for j in range(len(y[0])):
        result[i][j] = x[i][j] + y[i][j]

print("Addition of Matrx:")
print(tabulate(result, tablefmt='simple_grid'))

#Multiplication in matrix
print("Multiplication of Matrix:")

print(tabulate(np.dot(x, y), tablefmt='simple_grid'))