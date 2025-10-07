"""
This file demonstrates two Dynamic Programming approaches to solving the
Fibonacci sequence: Memoization (top-down) and Tabulation (bottom-up).
"""

# --- Method 1: Memoization (Top-Down DP) ---

# A dictionary to act as our cache for the memoization function.
# Note: For more complex applications, it's often better to encapsulate 
# this cache within a class or pass it as a default argument to the function.
memo_cache = {}

def fib_memo(n):
    """
    Calculates the nth Fibonacci number using memoization (top-down DP).
    """
    # 1. If the value is in our cache, return it immediately
    if n in memo_cache:
        return memo_cache[n]
    
    # Base case
    if n <= 1:
        return n
    
    # 2. If not in cache, compute it recursively
    result = fib_memo(n-1) + fib_memo(n-2)
    
    # 3. Store the result in the cache before returning
    memo_cache[n] = result
    return result


# --- Method 2: Tabulation (Bottom-Up DP) ---

def fib_tab(n):
    """
    Calculates the nth Fibonacci number using tabulation (bottom-up DP).
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0

    # 1. Create a table to store results up to n
    table = [0] * (n + 1)
    
    # 2. Set the known base case
    table[1] = 1
    
    # 3. Iterate from the bottom up, filling the table
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
        
    # The final answer is the last entry in the table
    return table[n]


# --- Example Usage ---

if __name__ == "__main__":
    test_number = 15

    print("--- Dynamic Programming for Fibonacci ---")
    
    print(f"\nCalculating Fibonacci({test_number}) using Memoization:")
    # Clear the cache before running to ensure a clean test
    memo_cache.clear()
    result_memo = fib_memo(test_number)
    print(f"Result: {result_memo}")
    print(f"Cache state after: {memo_cache}")

    print(f"\nCalculating Fibonacci({test_number}) using Tabulation:")
    result_tab = fib_tab(test_number)
    print(f"Result: {result_tab}")

    # Demonstrate a larger number
    large_number = 50
    memo_cache.clear()
    print(f"\nFibonacci({large_number}) with Memoization: {fib_memo(large_number)}")
    print(f"Fibonacci({large_number}) with Tabulation:  {fib_tab(large_number)}")
