N = 4
G = {}
for i in range(N):
    v1, v2 = input('Enter to vertex: ').split()
    for v, u in (v1, v2), (v2, v1):
        if v not in G:
            G[v] = {u}
        else:
            G[v].add(u)