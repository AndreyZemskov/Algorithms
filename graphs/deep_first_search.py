def dfs(vertex, G, used=None):
    used = used or set()
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)

graf_example = {'A': {'C', 'B'}, 'B': {'A'},
                'C': {'E', 'A', 'D', 'K'}, 'D': {'G', 'F', 'I', 'C', 'H'},
                'K': {'C', 'N', 'M', 'L'}, 'E': {'C', 'R', 'P'},
                'F': {'D'}, 'G': {'D'}, 'H': {'D'}, 'I': {'D'},
                'M': {'K'}, 'L': {'K'}, 'N': {'K'}, 'P': {'E'}, 'R': {'E'}}

first_vertex = 'A'
used = {}
N = 0

for f in graf_example:
    if f not in used:
        dfs(first_vertex, graf_example, used)
        N += 1
print('Linked graphs:', N)