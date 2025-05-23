def quicksort(arr):
    # Base case: if the array has 1 or no elements, it is already sorted
    if len(arr) <= 1:
        return arr
    # Choose the pivot element (middle element of the array)
    pivot = arr[len(arr) // 2]
    # Partition the array into three parts: elements less than the pivot, equal to the pivot, and greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively apply quicksort to the left and right partitions and combine the results
    return quicksort(left) + middle + quicksort(right)

# Example usage
if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", sample_array)
    sorted_array = quicksort(sample_array)
    print("Sorted array:", sorted_array)