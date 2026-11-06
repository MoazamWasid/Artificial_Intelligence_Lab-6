class Graph:
    def __init__(self, vertices):
        self.V = vertices + 1
        self.adj = [[] for i in range(self.V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def DFS(self, start):
        visited = [False] * self.V
        stack = [start]

        while stack:
            node = stack.pop()

            if not visited[node]:
                visited[node] = True
                print(node, end=" ")

                for neighbor in reversed(self.adj[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)


g = Graph(12)

g.addEdge(1, 2)
g.addEdge(1, 7)
g.addEdge(1, 8)

g.addEdge(2, 3)
g.addEdge(2, 6)

g.addEdge(3, 4)
g.addEdge(3, 5)

g.addEdge(8, 9)
g.addEdge(8, 12)

g.addEdge(9, 10)
g.addEdge(9, 11)

print("DFS Traversal:")
g.DFS(1)