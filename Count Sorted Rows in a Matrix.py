def count_sorted_rows(matrix):
    count = 0
    for row in matrix:
        if all(row[i] <= row[i + 1] for i in range(len(row) - 1)) or all(row[i] >= row[i + 1] for i in range(len(row) - 1)):
            count += 1
    return count
N, M = map(int, input().split())
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
result = count_sorted_rows(matrix)
print(result)
