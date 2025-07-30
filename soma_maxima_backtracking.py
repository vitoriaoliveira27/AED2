import sys
sys.setrecursionlimit(100000001)
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
    print("🧪 Starting tests for the Maximum Subarray Sum algorithm...")

    # Array grande com números positivos e negativos
    arr1 = [random.randint(-100, 100) for _ in range(10000)]
    print(f"Maximum sum found: {max_subarray_sum_backtracking(arr1)}")
    print("-" * 40)

    print("✅ Tests completed.")