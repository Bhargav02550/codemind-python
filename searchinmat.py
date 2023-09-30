def search_in_matrix(matrix, x):
  row = 0
  col = len(matrix[0]) - 1
  while row < len(matrix) and col >= 0:
    if matrix[row][col] == x:
      return True
    elif matrix[row][col] < x:
      row += 1
    else:
      col -= 1
  return False
rows = int(input())
cols = int(input())
matrix = []
for i in range(rows):
  row = list(map(int, input().split()))
  matrix.append(row)

x = int(input())
if search_in_matrix(matrix, x):
  print(1)
else:
  print(0)
