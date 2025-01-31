class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

def find_set(ds, vertex):
    if ds.parent[vertex] != vertex:
        ds.parent[vertex] = find_set(ds, ds.parent[vertex])
    return ds.parent[vertex]

def union(ds, vertex1, vertex2):
    root1 = find_set(ds, vertex1)
    root2 = find_set(ds, vertex2)

    if root1 != root2:
        if ds.rank[root1] > ds.rank[root2]:
            ds.parent[root2] = root1
        else:
            ds.parent[root1] = root2
            if ds.rank[root1] == ds.rank[root2]:
                ds.rank[root2] += 1