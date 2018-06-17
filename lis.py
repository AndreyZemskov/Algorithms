def lis(A):
    F = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        m = 0
        for j in range(0, i):
            if A[i - 1] > A[j - 1] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return(F[len(A)])