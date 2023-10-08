def product_combinations(N):
    count = 0
    for a in range(1, N):
        if N % a == 0:
            b = N // a
            if a < b:
                count += 1
    return count

# Input
N = int(input())

# Calculate and print the number of distinct product combinations
result = product_combinations(N)
print(result)
