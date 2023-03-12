# Bubble sort 

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

list = [24,13,15,54,89,65,456,12]
print("Unsorted Data", list)
bubble_sort(list)
print("Bubble Sort:",list)
print("Coded By Durani Mohammed Zaeem, Roll no: 425")

print()
print()

# Selection Sort
def selection_sort(arr):
    for item in range(len(arr)-1):
        mindex = item
        for j in range(mindex+1, len(arr)):
            if arr[j] < arr[mindex]:
                mindex = j
        (arr[item], arr[mindex]) = (arr[mindex], arr[item])

list = [24,13,15,54,89,65,456,12]
print("Unsorted Data", list)
selection_sort(list)
print("Selection Sort:",list)
print("Coded By Durani Mohammed Zaeem, Roll no: 425")



print()
print()


# Insertion Sort
def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1]=key

list = [24,13,15,54,89,65,456,12]
print("Unsorted Data", list)
insertion_sort(list)
print("Insertion Sort:",list)
print("Coded By Durani Mohammed Zaeem, Roll no: 425")


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2    # Finding the mid of the array
        L = arr[:mid]        # Dividing the array elements
        R = arr[mid:]        # into 2 halves
        mergeSort(L)         # Sorting the first half
        mergeSort(R)         # Sorting the second half
        i = j = k = 0
        while i < len(L) and j < len(R):    # Copy data to temp arrays L[] and R[]
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        while i < len(L):                   # Checking if any element was left
            arr[k] = L[i]
            i += 1
            k += 1
    
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Driver Code
if __name__ == '__main__':
    print()
    print()
    print("Merge Sort Algorithm implementation")
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", arr)
    mergeSort(arr)
    print("Sorted array is: ", arr)
    print("Coded by Durani Mohammed Zaeem, Roll no: 425")
