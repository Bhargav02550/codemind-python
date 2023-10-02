def find_distinct_elements(arr1, arr2):
    # Convert the input arrays into sets
    set1 = set(arr1)
    set2 = set(arr2)

    # Find the distinct elements in each set
    ans1 = list(set1 - set2)
    ans2 = list(set2 - set1)

    return ans1, ans2

# Input
N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Calculate and print the result
result1, result2 = find_distinct_elements(arr1, arr2)
print(" ".join(map(str, result1)))
print(" ".join(map(str, result2)))
