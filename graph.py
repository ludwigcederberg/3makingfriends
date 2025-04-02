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

    def kruskal(self):
        
        pass

    def prims(self):
        pass