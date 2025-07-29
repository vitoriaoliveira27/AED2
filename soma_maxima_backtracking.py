import math
from typing import List
import random


def _backtrack_solve(index: int, arr: List[int], current_sum: int, max_so_far: int) -> int:
    """
    Recursive function that explores the array, deciding at each step whether to
    extend the current subarray or start a new one.

    Args:
        index (int): The current index being evaluated.
        arr (List[int]): The complete array.
        current_sum (int): The maximum sum of the subarray that ENDS at the previous index.
        max_so_far (int): The global maximum sum found anywhere in the array so far.

    Returns:
        int: The global maximum sum at the end of the exploration.
    """
    if index == len(arr):
        return max_so_far

    sum_ending_here = max(arr[index], current_sum + arr[index])

    new_max_so_far = max(max_so_far, sum_ending_here)

    return _backtrack_solve(index + 1, arr, sum_ending_here, new_max_so_far)

def max_subarray_sum_backtracking(arr: List[int]) -> int:
    """
    Main function to solve the problem using backtracking with pruning.
    (Recursive implementation of Kadane's Algorithm).
    """
    if not arr:
        return 0

    return _backtrack_solve(1, arr, arr[0], arr[0])

if __name__ == "__main__":
    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {arr1}")
    print(f"Maximum sum found: {max_subarray_sum_backtracking(arr1)} (Expected: 6)")
    print("-" * 40)

    arr2 = [-1]
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
