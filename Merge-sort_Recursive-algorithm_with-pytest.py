import pytest

def merge_sort(lst):
    """
    Recursively divides the input list into halves, sorts each half,
    and merges them back together in sorted order.
    """
    if len(lst) <= 1:
        return lst  # Base case: a list with 0 or 1 element is already sorted

    # Divide the list into two halves
    middle = len(lst) // 2
    left_half = merge_sort(lst[:middle])   # Recursively sort the left half
    right_half = merge_sort(lst[middle:])  # Recursively sort the right half

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists (left and right) into a single sorted list.
    """
    result = []  # This will hold the merged and sorted elements
    i = j = 0    # Pointers for left and right lists

    # Compare elements from both lists and add the smallest to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements (if any) from left or right
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Parameterized tests using pytest
@pytest.mark.parametrize("input_list, expected", [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, 3, 3], [3, 3, 3]),
    ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
    ([10, -1, 2, 5, 0], [-1, 0, 2, 5, 10]),
])
def test_merge_sort(input_list, expected):
    assert merge_sort(input_list) == expected
