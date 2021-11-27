def find_max(arr):
  if len(arr) == 1:
    return arr[0]
  temp = find_max(arr[1:])
  if arr[0] > temp:
    return arr[0]
  else:
    return temp

lst = [1,3,5,8,9,10,75]

max = find_max(lst)
print(max)

def binary_search_helper(lst, start, end, elem):
  if end < start:
    return None
  mid = (start + end) // 2
  if lst[mid] == elem:
    return mid
  elif elem < lst[mid]:
    return binary_search_helper(lst, start, mid-1, elem)
  else:
    return binary_search_helper(lst, mid+1, end, elem)

def binary_search(lst, elem):
  return binary_search_helper(lst, 0, len(lst)-1, elem)

index = binary_search(lst, 100)
print(index)

class Vertex:
  def __init__(self):
    self.val
    self.adjacencies = []
  
  def add_vertex(self, vertex):
    self.adjacencies.append(vertex)

vertex = Vertex()
vertex1 = Vertex()
vertex.add_vertex(vertex1)

print(vertex)
print(vertex1)