stack = Stack()
    # make a set for the visited nodes
    visited = set()
    path = []

    path.append(starting_vertex)

    stack.push(path)

    def helper(starting_vertex):
      if starting_vertex == None:
        return

      current_path = stack.pop() # [1]
      current_node = current_path[-1] # 1

      if current_node == destination_vertex: # 1 != 4
        return current_path
      else:
        if current_node not in visited:
          visited.add(current_node) # [1]

          edges = self.get_neighbors(current_node) # [2]
      
          for edge in edges:
            # if edge not in visited:
            copyPath = current_path.copy()
            copyPath.append(edge) #[1, 2]

            stack.push(copyPath) #[[1,2]]
            helper(edge) # helper(2)

    return helper(starting_vertex) # 1

# helper(2)
def helper(starting_vertex):
      if starting_vertex == None:
        return

      current_path = stack.pop() # [1,2]
      current_node = current_path[-1] # 2

      if current_node == destination_vertex: # 2 != 4
        return current_path
      else:
        if current_node not in visited:
          visited.add(current_node) # [1, 2]

          # will branch off
          edges = self.get_neighbors(current_node) # [3, 4]
      
          for edge in edges:
            # edge 3
            if edge not in visited:
              copyPath = current_path.copy()
              copyPath.append(edge) #[1, 2, 3]

              stack.push(copyPath) #[[1,2,3]]
              helper(edge) # helper(3)    returns None
          
          # edge 4
          if edge not in visited:
              copyPath = current_path.copy()
              copyPath.append(edge) #[1, 2, 4]

              stack.push(copyPath) #[[1,2,4]]
              helper(edge) # helper(4)    will branch off and return [1,2, 4]
              # seems to evaporate here, tho

# helper(3) deadend

# helper(4)
def helper(starting_vertex):
  if starting_vertex == None:
    return

  current_path = stack.pop() # [1,2, 4]
  current_node = current_path[-1] # 4

  if current_node == destination_vertex: # 4 != 4
    return current_path
    # should finish here
  else:
    if current_node not in visited:
      visited.add(current_node) # [1, 2]

      # will branch off
      edges = self.get_neighbors(current_node) # [3, 4]
  
      for edge in edges:
        if edge not in visited:
          copyPath = current_path.copy()
          copyPath.append(edge) #[1, 2, 3]

          stack.push(copyPath) #[[1,2,3]]
          helper(edge) # helper(3)    will branch off              