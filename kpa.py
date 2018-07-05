N = 3            # items
M = 10           # place in the backpack
m = [3, 4, 4, 5] # weight
v = [4, 5, 6, 6] # value

F = [[0] * (N + 1) for i in range(M + 1)]

for i in range(N + 1):
    for k in range(M + 1):
        if m[i] <= k:
            F[k][i] = max(F[k][i - 1], v[i] + F[k - m[i]][i - 1])
        else:
            F[k][i] = F[k][i - 1]
print(F[M][N])