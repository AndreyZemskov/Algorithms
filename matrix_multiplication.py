def matrix_multiplication(A:list, B:list):
    result = [[0] * len(A) for i in range(len(B))]
    for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(B)):
                   result[i][j] += A[i][k] * B[k][j]
                return result
