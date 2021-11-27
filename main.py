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

def dfs(graph, vertex, end, discovered, finished, path, solution):
  if vertex == end:
    path.append(vertex)
    return path
  if end in graph[vertex]:
    path += [vertex, end]
    return path
  
  discovered.append(vertex)
  path.append(vertex)
  for adjacent in graph[vertex]:
    if adjacent not in discovered and adjacent not in finished:
      path = dfs(graph, adjacent, end, discovered, finished, path, solution)
    if end in path:
      if len(solution) == 0:
        solution = list(path)
      elif len(path) < len(solution):
        solution = list(path)
      # Maybe is not yet finished
      path.remove(end)
      path.remove(adjacent)

  finished.append(vertex)
  return path

def shortest_path(graph, start, end):
  return dfs(graph, start, end, [], [], [], [])
    
path = shortest_path(graph, 6, 12)
print(path)