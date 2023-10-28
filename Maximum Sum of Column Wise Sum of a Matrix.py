def max_column_wise_sum(matrix, N, M):
    max_sum = 0

    for j in range(M):
        column_sum = sum(matrix[i][j] for i in range(N))
        max_sum = max(max_sum, column_sum)

    return max_sum
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = max_column_wise_sum(matrix, N, M)
print(result)
