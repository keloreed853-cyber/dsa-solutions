import heapq

class MaxHeap:
    """Implements a Max Heap using Python's min-heap module (heapq)
    by negating values to simulate max-heap behavior."""

    def __init__(self):
        # Stores negative values to force
        # min-heap logic to prioritize largest positive
        # numbers
        self._heap = []

    def push(self, item: int) -> None:
        """Adds an item to the heap in O(log n)
        time."""
        # Negate the item for insertion
        heapq.heappush(self._heap, -item)

    def pop(self) -> int:
        """Removes and returns the largest item
        in O(log n) time."""
        if not self._heap:
            raise IndexError("pop from empty heap")
        # Negate the result back to positive
        return -heapq.heappop(self._heap)

    def peek(self) -> int:
        """Returns the largest item without
        removal in O(1) time."""
        if not self._heap:
            raise IndexError("peek from empty heap")
        return -self._heap[0]

# Example Usage
max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(5)
max_heap.push(20)

print(f"Peek (Max Value): {max_heap.peek()}")
print(f"Pop: {max_heap.pop()}")
print(f"Pop: {max_heap.pop()}")
