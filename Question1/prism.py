from heapq import heappop, heappush
import networkx as nx
import matplotlib.pyplot as plt

def prim(graph):
    # Initialize the minimum spanning tree and the set of visited nodes
    mst = []
    visited = set()

    # Choose a starting node in graph
    start_node = list(graph.keys())[0]
    visited.add(start_node)

    # Initialize the priority queue with the edges connected to the starting node
    priority_queue = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node]]

    # Use a heap to efficiently select the minimum weight edge
    while priority_queue:
        weight, current_node, next_node = heappop(priority_queue)

        # If the next_node has not been visited, add the edge to the minimum spanning tree
        if next_node not in visited:
            visited.add(next_node)
            mst.append((current_node, next_node, weight))

            # Add the edges connected to the next_node to the priority queue
            for neighbor, weight in graph[next_node]:
                if neighbor not in visited:
                    heappush(priority_queue, (weight, next_node, neighbor))

    return mst

# Define the graph using the provided edges
edges = [
    ('a', 'c', 8), ('a', 'f', 5), ('a', 'l', 14),
    ('b', 'f', 20), ('b', 'd', 8), ('b', 'k', 47), ('b', 'h', 12),
    ('c', 'a', 8), ('c', 'i', 10), ('c', 'l', 8), ('c', 'g', 12),
    ('d', 'f', 94), ('d', 'b', 8), ('d', 'g', 22),
    ('e', 'i', 16), ('e', 'h', 8), ('e', 'l', 15),
    ('f', 'a', 5), ('f', 'i', 8), ('f', 'd', 94), ('f', 'b', 20), ('f', 'k', 16),
    ('g', 'c', 12), ('g', 'l', 13), ('g', 'j', 5), ('g', 'd', 22),
    ('h', 'e', 8), ('h', 'j', 16), ('h', 'l', 15), ('h', 'b', 12),
    ('i', 'c', 10), ('i', 'f', 8), ('i', 'e', 16),
    ('j', 'k', 5), ('j', 'h', 16), ('j', 'g', 5),
    ('k', 'j', 5), ('k', 'b', 47), ('k', 'f', 16),
    ('l', 'e', 15), ('l', 'h', 15), ('l', 'g', 13), ('l', 'c', 8), ('l', 'a', 14)
]

# Create an adjacency list representation of the graph
graph = {}
for edge in edges:
    node1, node2, weight = edge
    graph.setdefault(node1, []).append((node2, weight))
    graph.setdefault(node2, []).append((node1, weight))

# Find the minimum spanning tree using Prim's algorithm
minimum_spanning_tree = prim(graph)
# Print the minimum spanning tree
print(f"The Minimum Spanning Tree:\n {minimum_spanning_tree}")


# draw graph
G = nx.Graph()

# Adds edges to the graph along with their weights using the add_weighted_edges_from method
G.add_weighted_edges_from(edges) 

# Create a graph for the minimum spanning tree
MST = nx.Graph()
MST.add_weighted_edges_from(minimum_spanning_tree)

# set node position
node_position = nx.spring_layout(G)

# Draw the minimum spanning tree with edge weights
nx.draw(MST, node_position, with_labels=True, font_weight='bold', node_size=500, node_color='green', font_color='black', font_size=8, edge_color='red',)
mst_edge_labels = nx.get_edge_attributes(MST, 'weight')
nx.draw_networkx_edge_labels(MST, node_position, edge_labels=mst_edge_labels, font_color='blue')

# Display the graph
plt.show()
