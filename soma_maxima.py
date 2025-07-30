import math
from typing import List
import random

def _find_max_crossing_sum(arr: List[int], low: int, mid: int, high: int) -> int:
    """
    Finds the maximum sum of a subarray that MUST cross the midpoint of the array.
    Complexity: O(n)

    Args:
        arr (List[int]): The full array.
        low (int): The starting index of the subarray to consider.
        mid (int): The midpoint index.
        high (int): The ending index of the subarray to consider.

    Returns:
        int: The maximum sum of a subarray crossing the midpoint.
    """
    current_sum = 0
    max_left_sum = -math.inf

    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > max_left_sum:
            max_left_sum = current_sum

    current_sum = 0
    max_right_sum = -math.inf

    for i in range(mid + 1, high + 1):
        current_sum += arr[i]
        if current_sum > max_right_sum:
            max_right_sum = current_sum

    return max_left_sum + max_right_sum

def _find_max_subarray_recursive(arr: List[int], low: int, high: int) -> int:
    """Recursive helper function that implements the Divide and Conquer logic."""

    if low == high:
        return arr[low]

    mid = (low + high) // 2

    max_sum_left = _find_max_subarray_recursive(arr, low, mid)
    max_sum_right = _find_max_subarray_recursive(arr, mid + 1, high)

    max_sum_crossing = _find_max_crossing_sum(arr, low, mid, high)
    
    return max(max_sum_left, max_sum_right, max_sum_crossing)


def max_subarray_sum(arr: List[int]) -> int:
    """
    Main function to solve the Maximum Subarray Problem
    using the Divide and Conquer paradigm.

    Args:
        arr (List[int]): A list of integers (positive and/or negative).

    Returns:
        int: The sum of the contiguous subarray with the largest sum.
    """
    if not arr:
        return 0

    return _find_max_subarray_recursive(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    print("🧪 Starting tests for the Maximum Subarray Sum algorithm...")

    # Array grande com números positivos e negativos
    arr1 = [random.randint(-100, 100) for _ in range(10000)]
    print(f"Maximum sum found: {max_subarray_sum(arr1)}")
    print("-" * 40)

    print("✅ Tests completed.")