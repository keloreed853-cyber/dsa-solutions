
import math

def _is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check for odd divisors from 3 up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    """
    Filters a list of integers and returns a new list containing only the prime numbers.

    Complexity:
        O(N * sqrt(M)) where N is the number of elements in the input list,
        and M is the value of the largest number in the list. This is because
        for each of the N numbers, we perform a primality test that takes
        up to sqrt(M) time.

    Examples:
        >>> filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        [2, 3, 5, 7]

        >>> filter_primes([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        [11, 13, 17, 19]
    """
    return [num for num in numbers if _is_prime(num)]

# Example Usage:
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    primes1 = filter_primes(list1)
    print(f"Original list: {list1}")
    print(f"Prime numbers: {primes1}")

    print("-" * 20)

    list2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    primes2 = filter_primes(list2)
    print(f"Original list: {list2}")
    print(f"Prime numbers: {primes2}")

