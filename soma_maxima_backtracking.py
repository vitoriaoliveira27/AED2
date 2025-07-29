import math
from typing import List
import random


def _explore_from(current_index: int, current_sum: int, arr: List[int], max_sum_container: List[float]):
    """
    Recursive function that explores all subarrays starting from a given point.
    This is the essence of the "backtracking" approach for this problem.

    Args:
        current_index (int): The index of the element being added to the subarray.
        current_sum (int): The sum of the subarray built up to the previous step.
        arr (List[int]): The complete original list.
        max_sum_container (List[float]): A mutable container to hold the maximum sum found globally.
    """
    if current_index >= len(arr):
        return
    
    new_subarray_sum = current_sum + arr[current_index]

    max_sum_container[0] = max(max_sum_container[0], new_subarray_sum)

    _explore_from(current_index + 1, new_subarray_sum, arr, max_sum_container)

def max_subarray_sum_backtracking(arr: List[int]) -> int:
    """
    Main function to solve the Maximum Subarray Problem
    using the Backtracking paradigm (recursive exhaustive search).

    Args:
        arr (List[int]): A list of integers.

    Returns:
        int: The value of the sum of the contiguous subarray with the largest value.
    """
    if not arr:
        return 0

    max_sum_container = [-math.inf]

    for i in range(len(arr)):
        _explore_from(i, 0, arr, max_sum_container)

    return int(max_sum_container[0])

if __name__ == "__main__":
    print("🧪 Starting tests for the Maximum Subarray Sum algorithm with Backtracking...")
    
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"\nArray: {arr1}")
    print(f"Maximum sum found: {max_subarray_sum_backtracking(arr1)} (Expected: 6)")
    print("-" * 40)

    arr2 = [-10, -1, -5, -2, -8]
    print(f"Array: {arr2}")
    print(f"Maximum sum found: {max_subarray_sum_backtracking(arr2)} (Expected: -1)")
    print("-" * 40)
    
    arr3 = [1, 2, 3, 4, 5]
    print(f"Array: {arr3}")
    print(f"Maximum sum found: {max_subarray_sum_backtracking(arr3)} (Expected: 15)")
    print("-" * 40)
    
    arr4 = []
    print(f"Array: {arr4}")
    print(f"Maximum sum found: {max_subarray_sum_backtracking(arr4)} (Expected: 0)")
    print("-" * 40)
    
    # Array grande com números positivos e negativos
    arr5 = [random.randint(-100, 100) for _ in range(100)]
    print(f"Array (100 elementos): {arr5}")
    print(f"Maximum sum found: {max_subarray_sum_backtracking(arr5)}")
    print("-" * 40)

    # Array grande com todos positivos
    arr6 = [random.randint(1, 100) for _ in range(200)]
    print(f"Array (200 elementos, positivos): {arr6}")
    print(f"Maximum sum found: {max_subarray_sum_backtracking(arr6)}")
    print("-" * 40)

    # Array grande com todos negativos
    arr7 = [random.randint(-100, -1) for _ in range(150)]
    print(f"Array (150 elementos, negativos): {arr7}")
    print(f"Maximum sum found: {max_subarray_sum_backtracking(arr7)}")
    print("-" * 40)

    print("✅ Tests completed.")