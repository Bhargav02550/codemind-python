# Python 3 program to find
# third Largest element in
# an array of distinct elements
import sys
def thirdLargest(arr, arr_size):

	# There should be
	# atleast three elements
	if (arr_size < 3):
	
		print(max(arr))
		return
	

	# Find first
	# largest element
	first = arr[0]
	for i in range(1, arr_size):
		if (arr[i] > first):
			first = arr[i]

	# Find second
	# largest element
	second = -sys.maxsize
	for i in range(0, arr_size):
		if (arr[i] > second and
			arr[i] < first):
			second = arr[i]

	# Find third
	# largest element
	third = -sys.maxsize
	for i in range(0, arr_size):
		if (arr[i] > third and
			arr[i] < second):
			third = arr[i]

	print(third)

# Driver Code
m=int(input())
arr = list(map(int,input().split()))
n = len(arr)
thirdLargest(arr, n)

# This code is contributed
# by Smitha
