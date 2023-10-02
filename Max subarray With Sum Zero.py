def max_subarray_with_sum_zero(arr):
    max_length = 0
    sum_to_index = {}
    current_sum = 0

    for index, num in enumerate(arr):
        current_sum += num

        if current_sum == 0:
            max_length = index + 1

        if current_sum in sum_to_index:
            max_length = max(max_length, index - sum_to_index[current_sum])
        else:
            sum_to_index[current_sum] = index

    return max_length
N = int(input()) 
arr = list(map(int, input().split()))
result = max_subarray_with_sum_zero(arr)
print(result)
