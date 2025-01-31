
# # This code defines a function `tsp_branch_and_bound` that uses memoization to optimize the solution of the TSP.
# # The `graph` variable represents the distance matrix between stations. 
# # The output is the minimum cost for the vehicle to collect all equipment 
# # and return to campus without passing through a station twice.

import sys

# define the function that takes graph parameter as distance matrix
def tsp_branch_and_bound(graph):
    n = len(graph) # Get the number of vertices(stations) in the graph
    memo = {} # initialize memo variable to store the visited stations 

# define recursive function to solve the tsp(traveling salesman problem) using branch and bound
# passing two parameters visited_station(bitvisited_station representing visited stations) and pos (current position)

    def tsp_dp(visited_station, pos):
        if visited_station == (1 << n) - 1: # Checks if all stations have been visited (all bits in the visited_station are set to 1
            return graph[pos][0], [pos]  # Return to campus

        # check if the solution for this subproblem has already been computed
        if (visited_station, pos) in memo:
            return memo[(visited_station, pos)]

        min_cost = sys.maxsize # initialize min_cost to the maximum possible integer value
        optimal_path = [] # initialize an empty list to store the optimal path

        # iterates over all stations
        for i in range(n):
            if (visited_station >> i) & 1 == 0:  # If the i-th station is not visited
                new_visited_station = visited_station | (1 << i)
                cost, path = tsp_dp(new_visited_station, i) #  Recursively calls the function with the updated visited_station and the new position (i).
                cost += graph[pos][i] # Adds the cost of traveling from the current position to the i-th station

                # Checks if the current path is better (lower cost) than the previously found minimum cost
                if cost < min_cost:
                    min_cost = cost  # Updates the minimum cost
                    optimal_path = [pos] + path

        # Stores the computed result in the memo dictionary for future reference.
        memo[(visited_station, pos)] = (min_cost, optimal_path)
        return min_cost, optimal_path

    initial_station = 1  # Start with the first station(Sets the initial bitvisited_station to 1, indicating that the algorithm starts from the first station.)
    return tsp_dp(initial_station, 0)

# define find_optimal route that take two parameters cities(takes a list of city names) and distance matrix as input
def find_optimal_route(cities, distance_matrix):
    min_cost, optimal_path = tsp_branch_and_bound(distance_matrix)

    # Map indices to city names
    city_names = [cities[i] for i in optimal_path]

    return min_cost, city_names

# define given cities name
cities = ["ALU", "Kigali CBD", "Kanombe", "Kimironko", "Kaciru"]

# Define graph representing the distances between stations
graph = [
    [0, 10, 8, 9, 7],
    [10, 0, 10, 5, 6],
    [8, 10, 0, 8, 9],
    [9, 5, 8, 0, 6],
    [7, 6, 9, 6, 0]
]

# call the find_optimal_route to find min_cost and optimal route
min_cost, optimal_route= find_optimal_route(cities, graph)

# print the optimal route and minimum/least cost
print("Optimal Route:", optimal_route)
print("Minimum/least Cost:", min_cost)