def main():
    G = read_graph()
    start = input('Which top to start with ?')

    while start not in G:
        start = input('This top is not found. Which top to start with ?')
    shortest_distances = dijkstra(G, start)

def read_graph():
    M = int(input('Number of edges: ')) # M - количество ребер, далее - строки "A B вес"
    G = {}
    for i in range(M):
        a, b, weight = input('Enter the vertices and the weight: ').split()
        weight = int(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

from collections import deque
def dijkstra(G, start):
    Q = deque()
    S = {}
    S[start] = 0
    Q.append(start)
    while Q:
        v = Q.pop()
        for u in G[v]:
            if u not in S or S[v] + G[v][u] < S[u]:
                S[u] = S[v] + G[v][u]
                Q.append(u)
                print(S)

if __name__ == '__main__':
    main()