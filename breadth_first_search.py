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

def breadth_first_search(graph, vertex):
  vertex_to_visit = []
  vertex_visited = set()
  vertex_to_visit.append(vertex)
  while vertex_to_visit:
    print(vertex_to_visit)
    vertex = vertex_to_visit.pop(0)
    print(vertex)
    vertex_visited.add(vertex)
    for adjacen in graph[vertex]:
      if adjacen not in vertex_visited and adjacen not in vertex_to_visit:
        vertex_to_visit.append(adjacen)
    print(vertex_visited)
  return len(vertex_visited)

num_of_vertices = breadth_first_search(graph, 4)
print(num_of_vertices)