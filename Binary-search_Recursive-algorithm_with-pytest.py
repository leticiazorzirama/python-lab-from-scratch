# Recursive binary search algorithm to find the index of an element in a sorted list

import pytest
from typing import List, Optional, Union

# Recursive binary search function with type annotations
def binary_search(
    lst: List[int],
    element: int,
    min: int = 0,
    max: Optional[int] = None
) -> Union[int, bool]:
    # Initialize max if not provided
    if max is None:
        max = len(lst) - 1

    # Check if the search interval is invalid (element not found)
    if max < min:
        return False
    else:
        # Calculate the middle index
        middle = min + (max - min) // 2

    # Search left half
    if lst[middle] > element:
        return binary_search(lst, element, min, middle - 1)

    # Search right half
    elif lst[middle] < element:
        return binary_search(lst, element, middle + 1, max)

    # Element found
    else:
        return middle

# Sample sorted list for testing
sample_list: List[int] = [10, 20, 30, 40, 50, 60]

# Parameterized tests using pytest
@pytest.mark.parametrize("lst, element, expected", [
    (sample_list, 10, 0),
    (sample_list, 20, 1),
    (sample_list, 30, 2),
    (sample_list, 40, 3),
    (sample_list, 50, 4),
    (sample_list, 60, 5),
    (sample_list, 25, False),
    (sample_list, 70, False),
    (sample_list, 5, False)
])
def test_binary_search(lst: List[int], element: int, expected: Union[int, bool]) -> None:
    assert binary_search(lst, element) == expected
