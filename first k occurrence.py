def find_first_k_occurrence(arr, k):
    element_count = {}
    
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
        
        if element_count[element] >= k:
            return element
    
    return -1

# Input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Find the first element that occurs at least k times
result = find_first_k_occurrence(arr, k)

# Output
print(result)
