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

def earliest_ancestor(ancestors, starting_node):
  
  # cuz we only search parents. 
  # essentially the get neighbors part of the problem
  def getParents(child):
    parents = []

    for tup in ancestors:
      if tup[1] == child:
        parents.append(tup[0])

    return parents

  # if it doesnt have parents, return -1
  # no need to do the work if there's none to be done
  if len(getParents(starting_node)) == 0:
    return -1

  stack = Stack()
  visited = set()

  path = [starting_node]
  longPath = path

  stack.push(path)

  while stack.size() > 0:
    current_path = stack.pop()
    # print(current_path)
    current_node = current_path[-1]

    # if current_path is longer,
    # we know it has some sort of parent
    if len(current_path) > len(longPath):
      longPath = current_path
    # if current_path is equal, we have to choose the smaller parent
    elif len(current_path) == len(longPath):
      if current_node < longPath[-1]:
        longPath = current_path
    
    if current_node not in visited:
      visited.add(current_node)
      edges = getParents(current_node)
      for edge in edges:
        copyPath = current_path.copy()
        copyPath.append(edge)
        stack.push(copyPath)

  return longPath[-1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 8))