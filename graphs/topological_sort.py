def dfs_sort(start, G, visited, ans):
    visited[start] = True
    for u in G:
        if not visited[u]:
            dfs_sort(u, G, visited, answer)
    ans.append(start)

vertex = 9
visited = [False] * (vertex + 1)
answer = []
graf = {5: {'C', 'B', 'D'}, 8: {'A'},
        7: {'A', 'E'}, 4: {'S', 'A', 'I'},
        9: {'C', 'G', 'F'}, 6: {'E'},
        2: {'E'}, 1: {'D'}, 3: {'D'}}

for i in range(1, vertex + 1):
    if not visited[i]:
        dfs_sort(i, graf, visited, answer)

answer[:] = answer[:: - 1]
print(answer)