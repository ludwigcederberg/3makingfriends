import sys
from graph import Graph

def process_input(input_data):
    lines = []
    for line in input_data.splitlines():
        lines.append(line)
    return lines

    
def main():
    
    input_data = open("data/sample/2.in", "r").read().strip()
    # input_data = sys.stdin.read().strip()
    input_list = process_input(input_data)

    header = input_list[0].split()
    num_nodes = int(header[0])
    num_edges = int(header[1])
    data = input_list[1:]

    graph = Graph(num_nodes)

    for line in data:
        edge = line.split()
        graph.add_edge(int(edge[0]) - 1, int(edge[1]) - 1, int(edge[2]))
    
    graph.sort_edges()
    print(graph.edge_order)
        
if __name__ == "__main__":
    main()