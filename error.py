### Graph - Adjacency list rep.
# import random
import queue

### Adjacency Matrix
adjacency_matrix = [[0, 1, 1, 1, 0, 0, 0, 0], 
                    [1, 0, 0, 0, 0, 1, 0, 1], 
                    [1, 0, 0, 1, 1, 0, 0, 1], 
                    [1, 0, 1, 0, 1, 0, 0, 0], 
                    [0, 0, 1, 1, 0, 0, 1, 1], 
                    [0, 1, 0, 0, 0, 0, 1, 1], 
                    [0, 0, 0, 0, 1, 1, 0, 0], 
                    [0, 1, 1, 0, 1, 1, 0, 0]]

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

graph = adjacency_list

def breadth_first_search(graph, vertex):
  vertex_to_check = []
  vertex_checked = set()
  vertex_to_check.append(vertex)
  while vertex_to_check:
    print(vertex_to_check)
    print(vertex)
    for adjacen in graph[vertex]:
      if adjacen not in vertex_checked and adjacen not in vertex_to_check:
        vertex_to_check.append(adjacen)
    vertex_checked.add(vertex)  
    vertex = vertex_to_check.pop(0)
    print(vertex_checked)
  return len(vertex_checked)

vertices = breadth_first_search(graph, 4)
print(vertices)