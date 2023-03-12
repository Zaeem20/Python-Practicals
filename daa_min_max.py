import time
import random

def quick_sort(collection: list) -> list:
    if len(collection) < 2:
        return collection
    pivot_index = random.randrange(len(collection))  # Use random element as pivot
    pivot = collection[pivot_index]
    greater: list[int] = []  # All elements greater than pivot
    lesser: list[int] = []  # All elements less than or equal to pivot

    for element in collection[:pivot_index]:
        (greater if element > pivot else lesser).append(element)

    for element in collection[pivot_index + 1 :]:
        (greater if element > pivot else lesser).append(element)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.perf_counter()
    sorted = quick_sort(unsorted)
    end = time.perf_counter()
    
    print("Quick Sort Algorithm:")
    print('Sorted data:', sorted)
    print(f'Minimum in List: {sorted[0]}')
    print(f'Maximum in List: {sorted[-1]}')

    print(f'Time taken {round((end-start)*1000, 3)}ms')
    print("\nCoded By Durani Mohammed Zaeem, Roll no: 425")