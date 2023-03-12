def linear_search(value, arr):
    for idx, item in enumerate(arr):
        if item == value:
            return idx
    return -1

print("Linear Searching")
search = linear_search(67, data := [78,64,33,42,67,82,99])
print('List:', data)
if not search:
    print("No Element Found")
else:
    print(f"Element Found at Index: {search}")

print("Coded By Durani Mohammed Zaeem, Roll no: 425")

print()
print()
print()

def binary_search(sorted_collection: list[int], item: int):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None

search = binary_search(data := [16,17,18,22,25,36,42], 18)

print('List:', data)

print("Binary Searching")
if not search:
    print("No Element Found")
else:
    print(f"Element Found at Index: {search}")
print("Coded By Durani Mohammed Zaeem, Roll no: 425")
