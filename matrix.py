import numpy

def row_sum(arr):
    sum = 0
    row, col = numpy.shape(arr)
    print('Finding Sum of each rows:')
    for i in range(row):
        for j in range(col):
            sum+=arr[i][j]
        print(f'Row {i+1} sum will be:', sum)
        sum=0

def col_sum(arr):
    sum = 0
    row, col = numpy.shape(arr)
    print('Finding sum of each column')
    for i in range(row):
        for j in range(col):
            sum+=arr[j][i]
        print(f'Column {i+1} sum will be', sum)
        sum=0

import numpy as np

arr = np.zeros((4,4), dtype='I')
row , col = np.shape(arr)
x = 1
for i in range(row):
    for j in range(col):
        arr[i][j]=x
        x+=1

row_sum(arr)
col_sum(arr)