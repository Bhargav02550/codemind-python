def is_possible(N):
    for x in range(N // 2 + 1):
        y = (N - 2 * x) / 7
        if y.is_integer() and y >= 0:
            return "YES"  
    return "NO" 
N = int(input())
result = is_possible(N)
print(result)
