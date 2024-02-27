def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
if __name__ == "__main__":
    # Input array
    unsorted_array = [5, 2, 4, 6, 1, 3]

    print("Original Array:", unsorted_array)

    # Sorting the array using Insertion Sort
    insertion_sort(unsorted_array)

    print("Sorted Array:", unsorted_array)
