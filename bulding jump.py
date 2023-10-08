import math
def find_consecutive_steps(arr, len):
	count = 0
	maximum = 0
	for index in range(1, len):
		if (arr[index] > arr[index - 1]):
			count += 1

		else:
			maximum = max(maximum, count)
			count = 0
	return max(maximum, count)
n = int(input())
arr = list(map(int,input().split()))
len = len(arr)
print(find_consecutive_steps(arr, len))
