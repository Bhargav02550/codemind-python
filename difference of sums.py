def difference_of_sums(N):
    sum_of_squares = sum(i**2 for i in range(1, N + 1))
    square_of_sum = sum(range(1, N + 1))**2
    return abs(sum_of_squares - square_of_sum)
N = int(input())
result = difference_of_sums(N)
print(result)
