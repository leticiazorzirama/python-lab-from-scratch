# Sorts a list of elements in ascending order using the Insertion Sort algorithm.

def insertion_sort(arr):
    # Iterate over the list starting from the second element (index 1)
    for index in range(1, len(arr)):
        current_value = arr[index]  # Store the value to be positioned correctly
        position = index            # Track the index where current_value should be inserted

        # Shift elements of the sorted portion of the list to the right
        # until the correct position for current_value is found
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]  # Move the larger element one position to the right
            position -= 1                      # Move one position left to continue comparing

        # Insert the current_value at its correct position
        arr[position] = current_value

    return arr


# Tests using assert
assert insertion_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
assert insertion_sort([10, -3, 0, 7, 4]) == [-3, 0, 4, 7, 10]
assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert insertion_sort([3]) == [3]
assert insertion_sort([]) == []

print("All tests passed.")
