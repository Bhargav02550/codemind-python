def sum_of_diagonal(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    if n != m:
        return "Matrix is not square"
    
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]
        if i != n - 1 - i:
            diagonal_sum += matrix[i][n - 1 - i]
    
    return diagonal_sum
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
result = sum_of_diagonal(matrix)
print(result)
