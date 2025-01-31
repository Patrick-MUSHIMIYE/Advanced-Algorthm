# import matplotlib.pyplot as plt
# import numpy as np

# # Function for Bubble Sort time complexity T(n)
# def bubble_sort_time(n):
#     return n**2

# # Function for Selection Sort time complexity R(n)
# def selection_sort_time(n):
#     return n**2

# # Create an array of values for n
# n_values = np.arange(1, 10, 1)  # Change the range based on your needs

# # Calculate the corresponding values for T(n) and R(n)
# t_values = [bubble_sort_time(n) for n in n_values]
# r_values = [selection_sort_time(n) for n in n_values]

# # Plot the functions
# plt.plot(n_values, t_values, label='Bubble Sort (T(n))')
# plt.plot(n_values, r_values, label='Selection Sort (R(n))')

# # Add labels and a legend
# plt.xlabel('Input Size (n)')
# plt.ylabel('Number of Operations')
# plt.legend()

# # Show the plot
# plt.show()


import matplotlib.pyplot as plt
import timeit

def bubble_sort(arr):
    n = len(arr)

    for k in range(1, n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Measure execution time for different input sizes
input_sizes = list(range(1, 1001, 50))
bubble_sort_times = []
selection_sort_times = []

for size in input_sizes:
    arr_bubble = list(range(size, 0, -1))
    arr_selection = list(range(size, 0, -1))

    bubble_time = timeit.timeit(lambda: bubble_sort(arr_bubble.copy()), number=10)
    selection_time = timeit.timeit(lambda: selection_sort(arr_selection.copy()), number=10)

    bubble_sort_times.append(bubble_time)
    selection_sort_times.append(selection_time)

# Plot the results
plt.plot(input_sizes, bubble_sort_times, label='Bubble Sort')
plt.plot(input_sizes, selection_sort_times, label='Selection Sort')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.show()
