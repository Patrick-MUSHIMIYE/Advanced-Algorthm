# use kruskal's algorthm to find a minimum weight spanning
# Your answer should include a complete list of the edges,
# indicating which edges you take for your tree in the course of running the algorithm.

# edge = (a, c, 8), (a, f, 5), (a, l, 14), (b, f, 20), (b, d, 8), (b, k, 47), (b, h, 12), (c, a, 8), (c, i, 10), (c, l, 8), (c, g, 12), (d, f, 94), (d, b, 8), (d, g, 22), (e, i, 16), (e, h, 8), (e, l, 15), (f, a, 5), (f, i, 8), (f, d, 94), (f, b, 20), (f, k, 16), (g, c, 12), (g, l, 13), (g, j, 5), (g, d, 22), (h, e, 8), (h, j, 16), (h, l, 15), (h, b, 12), (i, c, 10), (i, f, 8), (i, e, 16), (j, k, 5), (j, h, 16), (j, g, 5), (k, j, 5), (k, b, 47), (k, f, 16), (l, e, 15),(l, h, 15), (l, g, 13), (l, c, 8), (l, a, 14)


import networkx as nx
import matplotlib.pyplot as plt


from disjointset import DisjointSet, find_set, union

def kruskal(edge_graph):
    vertices = set()
    edges = sorted(edge_graph, key=lambda x: x[2])
    minimum_spanning_tree = []

    for edge in edges:
        vertices.update([edge[0], edge[1]])

    ds = DisjointSet(vertices)

    for edge in edges:
        if find_set(ds, edge[0]) != find_set(ds, edge[1]):
            minimum_spanning_tree.append(edge)
            union(ds, edge[0], edge[1])

    return minimum_spanning_tree

# Initialize array of edges
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

# call kruskals and find Minimum Spanning Tree
min_spanning_tree = kruskal(edges)
print(f"The Minimum Spanning Tree: {min_spanning_tree}")
  
# draw original graph
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Create a graph for the minimum spanning tree
MST = nx.Graph()
MST.add_weighted_edges_from(min_spanning_tree)

# Draw the original graph with edge weights
start_position_node = nx.spring_layout(G)  

# Draw the minimum spanning tree with edge weights
nx.draw(MST, start_position_node, with_labels=True, font_weight='bold', node_size=700, node_color='green', font_color='black', font_size=8, edge_color='red',)
mst_edge_labels = nx.get_edge_attributes(MST, 'weight')
nx.draw_networkx_edge_labels(MST, start_position_node, edge_labels=mst_edge_labels, font_color='blue')

# Display the graph
plt.show()