
def quick_sort(arr):
    """
    Sorts an array in ascending order using the QuickSort algorithm.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quick_sort(my_list)
print(f"Unsorted list: {my_list}")
print(f"Sorted list: {sorted_list}")

"""
Time Complexity of QuickSort:

The time complexity of QuickSort depends on the choice of the pivot element, which determines how the array is partitioned at each step.

1. Best-Case Time Complexity: O(n log n)
   - This occurs when the pivot element chosen at each step divides the array into two roughly equal halves.
   - The recursion depth will be log(n), and at each level, we perform O(n) work for partitioning.
   - Total work: O(n * log n)

2. Average-Case Time Complexity: O(n log n)
   - On average, the pivot selection will lead to reasonably balanced partitions.
   - The mathematical analysis shows that even with some imbalance, the complexity remains O(n log n). It is one of the fastest sorting algorithms in practice for this reason.

3. Worst-Case Time Complexity: O(n^2)
   - This occurs when the pivot element is consistently the smallest or largest element in the (sub)array.
   - This leads to highly unbalanced partitions, where one sub-array has (n-1) elements and the other has 0.
   - The recursion depth becomes n, and at each level, we do O(n) work.
   - Total work: O(n * n) = O(n^2)
   - This worst-case scenario can happen if the array is already sorted or reverse-sorted and you always pick the first or last element as the pivot. The implementation above, which chooses the middle element, makes this specific scenario less likely but doesn't eliminate the possibility of a worst-case pivot choice.
"""
