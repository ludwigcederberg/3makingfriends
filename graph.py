class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[0] * self.nodes for _ in range(self.nodes)]
        self.edge_order = []  

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w
        self.edge_order.append([u, v, w])

    def sort_edges(self):
        self.edge_order.sort(key=lambda x: x[2])

    def jarnik(self):
        root = self.edge_order[0]
        visited = [root[0], root[1]]
        unvisited = self.edge_order[1:]

        while unvisited:
            v = unvisited[0]
            if (v[0] not in visited and v[1] not in visited):
                visited.append(v[0])
                continue
            if (v[0] in visited and v[1] not in visited):
                visited.append(v[1])
                continue
            if (v[0] not in visited and v[1] in visited):
                visited.append(v[0])
                continue
            
            unvisited = unvisited[1:]

    def kruskal(self):
        pass
