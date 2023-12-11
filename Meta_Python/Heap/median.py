import heapq
"""
The function `compute_medians` takes an array of numbers as input and returns a list of medians,
where each median is the median of the numbers seen so far.

Args:
    arr: The input array of numbers for which we want to compute the medians.

Returns:
    The function `compute_medians` returns a list of medians computed from the input array `arr`.
"""

def compute_medians(arr):
    max_heap = []  # Max-heap for the lower half
    min_heap = []  # Min-heap for the upper half
    medians = []

    for num in arr:
        # Add the number to the appropriate heap
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # Balance the heaps
        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        while len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Compute the median and add to the result
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2
        else:
            median = -max_heap[0]
        medians.append(int(median))

    return medians

# Example usage:
arr = arr = [5, 15, 1, 3]#[2, 1, 3, 7, 5]
result = compute_medians(arr)
print(result)  # Output: [2, 1, 2, 3, 3]
