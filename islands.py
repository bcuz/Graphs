# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

class Queue():
  def __init__(self):
    self.queue = []
  def enqueue(self, value):
    self.queue.append(value)
  def dequeue(self):
    if self.size() > 0:
      return self.queue.pop(0)
    else:
      return None
  def size(self):
    return len(self.queue)


def island_counter(matrix):
  queue = Queue()
  visited = set()
  
  path = [matrix[0][0]]

  queue.enqueue(path)

  while queue.size() > 0:
    current_path = queue.dequeue() 
    current_node = current_path[-1] 

    if current_node == destination_vertex:
      return current_path
    else:
      if current_node not in visited:
        visited.add(current_node)

        edges = self.get_neighbors(current_node)

        for edge in edges:
          if edge not in visited:
            copyPath = current_path.copy()
            copyPath.append(edge)
            queue.enqueue(copyPath)