# Bubble Sort algorithm: sorts a list by repeatedly comparing and swapping adjacent elements.

def bubble_sort(lst):
    """
    Implements the classic Bubble Sort algorithm.

    In each pass, the largest remaining element is "pushed" to the end of the list.
    The number of elements to be compared decreases progressively.
    """
    n = len(lst)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

def optimized_bubble_sort(lst):
    """
    Implements the Bubble Sort algorithm with an optimization: 
    if no swaps are made in a given iteration, the list is assumed to be sorted and the algorithm terminates early.
    """
    n = len(lst)

    for i in range(n - 1, 0, -1):
        swapped = False

        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break

    return lst

# Simple tests
if __name__ == "__main__":
    test_lists = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],   # already sorted
        [5, 4, 3, 2, 1],   # reverse sorted
        [],               # empty list
        [42],             # single element
        [3, 3, 3]          # all elements equal
    ]

    print("Testing bubble_sort:")
    for original in test_lists:
        lst = original.copy()
        print(f"Original: {original} → Sorted: {bubble_sort(lst)}")

    print("\nTesting optimized_bubble_sort:")
    for original in test_lists:
        lst = original.copy()
        print(f"Original: {original} → Sorted: {optimized_bubble_sort(lst)}")
