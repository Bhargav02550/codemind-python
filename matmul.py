# Function to perform matrix multiplication
def matrix_multiply(matrix1, matrix2):
    # Get the dimensions of the matrices
    M1, N1 = len(matrix1), len(matrix1[0])
    M2, N2 = len(matrix2), len(matrix2[0])

    # Check if the matrices can be multiplied
    if N1 != M2:
        return "Matrix multiplication is not possible."

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(N2)] for _ in range(M1)]

    # Perform matrix multiplication
    for i in range(M1):
        for j in range(N2):
            for k in range(N1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Input for the dimensions of the first matrix
M1, N1 = map(int, input().split())

# Input for the dimensions of the second matrix
M2, N2 = map(int, input().split())

# Input for the elements of the first matrix
matrix1 = []
for _ in range(M1):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Input for the elements of the second matrix
matrix2 = []
for _ in range(M2):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Perform matrix multiplication and print the result
result = matrix_multiply(matrix1, matrix2)
for row in result:
    print(*row)
