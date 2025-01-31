# import priorityQueue class from queue module
from queue import PriorityQueue

# define function designed to find the shortest path
def find_shortest_path(graph, current, visited, memo):
    if len(visited) == len(graph) - 1: # checks if all locations have been visited except the starting location ("A")
        return graph[current]["A"]  # All locations visited, return to starting location

    if (current, tuple(visited)) in memo:  # checks if the current state (current location and visited locations) is already in the memo dictionary
        return memo[(current, tuple(visited))]  # Return memoized result if available

 #  Initialize min_distance variable to be used to track the minimum distance during the exploration of paths
    min_distance = float('inf')

    # Use a priority queue to explore promising branches
    priority_queue = PriorityQueue()

    # Calculate lower bound for the branch
    for neighbor, distance in graph[current].items():
        if neighbor != "A" and neighbor not in visited:
            lower_bound = distance + find_lower_bound(graph, neighbor, visited)
            priority_queue.put((lower_bound, neighbor, distance))

    while not priority_queue.empty():
        _, next_node, distance = priority_queue.get()

        new_visited = visited.copy()
        new_visited.add(next_node)
        path_distance = distance + find_shortest_path(graph, next_node, new_visited, memo)
        min_distance = min(min_distance, path_distance)

    # Memoize the result
    memo[(current, tuple(visited))] = min_distance

    return min_distance

# Return the minimum edge weight from the current node to any unvisited node
def find_lower_bound(graph, current, visited):
    unvisited_nodes = [node for node in graph[current] if node != "A" and node not in visited]
    if not unvisited_nodes:
        return 0
    return min(graph[current][node] for node in unvisited_nodes)

# define create_graph function that take list of edges and construct graph
def create_graph(edges):
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = {}
        graph[edge[0]][edge[1]] = edge[2]
        if edge[1] not in graph:
            graph[edge[1]] = {}
        graph[edge[1]][edge[0]] = edge[2]
    return graph

# checks if the script is being run as the main program
if __name__ == "__main__":
  # initializes a list of edges representing a graph
    edges = [
        ("A", "B", 12),
        ("A", "C", 10),
        ("A", "D", 19),
        ("A", "E", 8),
        ("B", "C", 3),
        ("B", "D", 7),
        ("B", "E", 6),
        ("C", "D", 2),
        ("C", "E", 20),
        ("D", "E", 4),
    ]
 # creates the graph using the create_graph function,
 # sets the starting location to "A",
 # initializes an empty set for visited locations, and an empty dictionary for memoization
    graph = create_graph(edges)
    start_location = "A"
    visited = set()
    memo = {}
    shortest_path = find_shortest_path(graph, start_location, visited, memo)
    print(f"The shortest path for Sam to deliver items is: {shortest_path}")



# The running time of the algorthm,
# Since we're exploring promising branches, in the worst case the priority queue may have to consider all possible permutations of cities, leading to a time complexity of O(n!), where n is the number of cities.

# The algorithm uses memoization to store and retrieve computed results, which helps to avoid redundant calculations. In the best case, the algorithm may find the optimal solution early and terminate quickly due to memoization. In the worst case, the algorithm may still explore a significant portion of the solution space, resulting in an exponential time complexity.

# Overall, the time complexity is influenced by the effectiveness of the Branch and Bound, the structure of the input graph, and the specific characteristics of the problem instance. While memoization reduces redundant calculations, the worst-case time complexity is still exponential due to the nature of the traveling salesman problem.