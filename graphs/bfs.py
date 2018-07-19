N, M = map(int, input('Enter the vertices and edges: ').split())
print('You entering {} vertoces and {} edges'.format(N, M))
graph = {i: set() for i in range(N)}
for i in range(M):
    v1, v2 = map(int, input('Enter the coordinates of the edges: ').split())
    graph[v1].add(v2)
    graph[v2].add(v1)

from collections import deque
distances = [None] * N
start_vertex = 0
distances[start_vertex] = 0
queue = deque([start_vertex])

while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if  distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            queue.append(neigh_v)
            print(distances)