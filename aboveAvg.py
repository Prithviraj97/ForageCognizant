def above_average_subarrays(arr):
    n = len(arr)
    result = []

    # Calculate the prefix sum of the array
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    # Iterate through all subarrays
    for start in range(n):
        for end in range(start, n):
            subarray_sum = prefix_sum[end + 1] - prefix_sum[start]
            subarray_length = end - start + 1
            remaining_sum = prefix_sum[n] - subarray_sum
            remaining_length = n - subarray_length

            # Compare average sums
            subarray_average = subarray_sum / subarray_length if subarray_length > 0 else 0
            remaining_average = remaining_sum / remaining_length if remaining_length > 0 else 0

            if subarray_average > remaining_average:
                result.append((start + 1, end + 1))  # Adjust indices for output

    # Sort the result based on start and end indices
    result.sort()

    return result

# Example usage:
arr = [3, 1, 2, 4]
result = above_average_subarrays(arr)
print(result)
