def containsDuplicate(nums: list[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.

    This solution uses a hash set to achieve O(n) time complexity.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example Usage:
nums1 = [1, 2, 3, 1]
print(f"Input: {nums1}")
print(f"Output: {containsDuplicate(nums1)}") # Expected: True

nums2 = [1, 2, 3, 4]
print(f"Input: {nums2}")
print(f"Output: {containsDuplicate(nums2)}") # Expected: False

nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(f"Input: {nums3}")
print(f"Output: {containsDuplicate(nums3)}") # Expected: True
