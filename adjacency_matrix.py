N = 4
V = []
index = {}
A = [[0] * N for i in range(N)]
for i in range(N):
    v1, v2 = input('Enter to vertex: ').split()
    for v in v1, v2:
        if v not in index:
            V.append(v)
            index[v] = len(V) - 1
    v1_i = index[v1]
    v2_i = index[v2]
    A[v1_i][v2_i] = 1
    A[v2_i][v1_i] = 1