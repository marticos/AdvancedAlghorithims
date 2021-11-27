### Graph - Adjacency list rep.
# import random
import queue

### Adjacency Matrix
adjacency_matrix = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                    [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def adjacency_matrix_to_list(adjacency_matrix):
  num_of_vertecies = len(adjacency_matrix)
  adjacency_list = []
  for i in range(num_of_vertecies):
    adjacency_row = []
    for j in range(num_of_vertecies):
      if adjacency_matrix[i][j]:
        adjacency_row.append(j)
    adjacency_list.append(adjacency_row)
  return adjacency_list

adjacency_list = adjacency_matrix_to_list(adjacency_matrix)
print(adjacency_list)

print()

graph = adjacency_list

def dfs(graph, vertex, discovered, finished):
  discovered.append(vertex)
  for adjacen in graph[vertex]:
    if adjacen not in discovered:
      dfs(graph, adjacen, discovered, finished)
  finished.append(vertex)
  return len(discovered)

def depth_first_search(graph, vertex):
  return dfs(graph, vertex, [], [])
    
num_of_vertices = depth_first_search(graph, 4)
print(num_of_vertices)