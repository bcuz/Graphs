# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [
      [0, 1, 0, 1, 0],
      [1, 1, 0, 1, 1],
      [0, 0, 1, 0, 0],
      [1, 0, 1, 0, 0],
      [1, 1, 0, 0, 0]]
big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
         [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
         [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
         [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# nodes: 1's
# edges: NSEW neighbors, not diagonals
# connected components: islands

class Stack():
  def __init__(self):
    self.stack = []
  def push(self, value):
    self.stack.append(value)
  def pop(self):
    if self.size() > 0:
      return self.stack.pop()
    else:
      return None
  def size(self):
    return len(self.stack)

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

# checks cardinal directions for any neighbors
# dft() below will keep looping until entire island is 'mapped out'
def getNeighbors(matrix, node):
  # (0, 1) as example
  row = node[0]
  col = node[1]

  neighboring_islands = []

  stepNorth = stepSouth = stepWest = stepEast = False

  # the other spots on the matrix that we'll check
  # no
  if row > 0:
    stepNorth = row - 1
  if col > 0:
  # col 0 (will check that spot)
    stepWest = col - 1
  if row < len(matrix) - 1:
    # row 1
    stepSouth = row + 1
  if col < len(matrix) - 1:
    # col 2
    stepEast = col + 1

  if stepNorth is not False and matrix[stepNorth][col] == 1:
    neighboring_islands.append((stepNorth, col))

  if stepSouth is not False and matrix[stepSouth][col] == 1:
    # cardinally, this is the only spot that has a 1 in it
    # (1, 1)
    neighboring_islands.append((stepSouth, col))

  if stepWest is not False and matrix[row][stepWest] == 1:
    neighboring_islands.append((row, stepWest))

  if stepEast is not False and matrix[row][stepEast] == 1:
    neighboring_islands.append((row, stepEast))

  return neighboring_islands

def bft(matrix, node, visited):
  stack = Stack()
  stack.push(node)

  queue = Queue()
  queue.enqueue(node)

  while queue.size() > 0:
    current_node = queue.dequeue()

    if current_node not in visited:
      visited.add(current_node)

      edges = getNeighbors(matrix, current_node)
      for edge in edges:
        queue.enqueue(edge)

def islands_counter(matrix):
  total_islands = 0
  visited = set()
  # iterate through the matrix
  # if it's a 1, then we run DFT/BFT
  for row in range(len(matrix)):
    # we're concerned w/ the row length here
    # if the island is always X by X it doesnt matter
    for col in range(len(matrix[0])):
      node = (row, col)
      if node not in visited and matrix[row][col] == 1:
        bft(matrix, node, visited)
        # cuz dft() will find the entire island
        total_islands +=1

  return total_islands

print(islands_counter(islands))
print(islands_counter(big_islands))