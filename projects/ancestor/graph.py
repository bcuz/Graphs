"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import math

class Graph:

  """Represent a graph as a dictionary of vertices mapping labels to edges."""
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex_id):
    """
    Add a vertex to the graph.
    """
    self.vertices[vertex_id] = set()

  def add_edge(self, v1, v2):
    """
    Add a directed edge to the graph.
    """
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)

  def get_neighbors(self, vertex_id):
    """
    Get all neighbors (edges) of a vertex.
    """
    return self.vertices[vertex_id]

  # visiting current neighbors first,
  # then visiting those neighbors
  def bft(self, starting_vertex):
    """
    Print each vertex in breadth-first order
    beginning from starting_vertex.
    """
    # make a queue
    queue = Queue()
    # make a set for the visited nodes
    visited = set()

    # put our starting node in line
    queue.enqueue(starting_vertex)

    # if our queue's not empty, we have more people to visit!
    while queue.size() > 0:
      # get the next node out of line
      current_node = queue.dequeue()

      # check if it has been visited
      if current_node not in visited:
      ## if not, mark as visited
        visited.add(current_node)
        print(current_node)
      ## and get its neighbors
        edges = self.get_neighbors(current_node)
      ## put them in line to be visited
        for edge in edges:
          queue.enqueue(edge)

  def dft(self, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    # make a stack
    stack = Stack()
    # make a set for the visited nodes
    visited = set()

    # put our starting node on top of the stack
    stack.push(starting_vertex)

    # if our stack's not empty, we have more people to visit!
    while stack.size() > 0:
      # get the next node off the top of our stack
      current_node = stack.pop()

      # check if it has been visited
      if current_node not in visited:
      ## if not, mark as visited
        visited.add(current_node)
        print(current_node)
      ## and get its neighbors
        edges = self.get_neighbors(current_node)
      ## stack them on the stack to be visited
        for edge in edges:
          stack.push(edge)


  def dft_recursive(self, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.

    This should be done using recursion.
    """
    visited = set()
    
    def helper(starting_vertex):
      if starting_vertex == None:
        return

      print(starting_vertex)

      visited.add(starting_vertex)

      edges = self.get_neighbors(starting_vertex)
      # print(starting_vertex, edges)
      
      for edge in edges:
        if edge not in visited:
          helper(edge)

    helper(starting_vertex)
      
  # had to watch until 34:45 of https://www.youtube.com/watch?v=aWoLa0UisNs&feature=youtu.be
  # def bfs(self, starting_vertex, destination_vertex):
  def bfs(self, starting_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """

    # make a queue
    # make a set for visited

    # enqueue A PATH TO the starting_vertex

    # while the queue isn't empty:
    ## dequeue the next path
    ## current_node is the last thing in the path
    ## check if it's the target, aka the destination_vertex
    ## if so, return the path!!

    ## if not, mark this as visited
    ## get the neighbors
    ## copy the path, add the neighbor to the copy
    ## for each one, add a PATH TO IT to our queue

    queue = Queue()
    visited = set()
    path = []

    path.append(starting_vertex)

    queue.enqueue(path)

    while queue.size() > 0:
      current_path = queue.dequeue() 
      # print(queue.queue)
      # first one is the one being dequeued, seconds one is what remains in queue
      # gets [1,2], becomes []
      # gets [1,2,3], becomes [[1,2,4]]
      # gets [1,2,4] becomes [[1,2,3,5]]
      # gets [1,2,3,5], becomes [[1,2,4,6], [1,2,4,7]]
      # gets [1,2,4,6] becomes [[1,2,4,7]]
      current_node = current_path[-1] 
      # 2
      # 3
      # 4
      # 6

      # if current_node == destination_vertex:
      #   return current_path
      if current_node not in visited:
        visited.add(current_node)

        edges = self.get_neighbors(current_node)
        # print(edges)

        for edge in edges:
          if edge not in visited:
            copyPath = current_path.copy()
            copyPath.append(edge)
            # print(copyPath)
            # path.append(copyPath)
            queue.enqueue(copyPath)

  # def dfs(self, starting_vertex, destination_vertex):
  def dfs(self, starting_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    stack = Stack()
    visited = set()

    path = []

    path.append(starting_vertex)

    stack.push(path)

    lowest = math.inf

    while stack.size() > 0:      
      current_path = stack.pop()
      current_node = current_path[-1]

      # print(current_path, current_node)

      # would need to return the 
      # if current_node == destination_vertex:
      #   return current_path
      # else:
      if current_node not in visited:
        visited.add(current_node)
        edges = self.get_neighbors(current_node)

        if len(edges) > 1:
          for edge in edges:
            if edge < lowest:
              lowest = edge
        elif len(edges) == 1:
          lowest = next(iter(edges), None)

        for edge in edges:
          if edge not in visited:          
            copyPath = current_path.copy()
            copyPath.append(edge)
            stack.push(copyPath)

    if lowest == math.inf:
      return -1 
    return lowest

  def dfs_recursive(self, starting_vertex, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.

    This should be done using recursion.
    """
    stack = Stack()
    # make a set for the visited nodes
    visited = set()
    path = []

    path.append(starting_vertex)

    stack.push(path)

    def helper(starting_vertex):
      if starting_vertex == None:
        return

      current_path = stack.pop()
      current_node = current_path[-1]

      # print(5, visited)

      if current_node == destination_vertex:
        # for some reason isnt being returned at the end.
        # print(current_path)
        return current_path

      else:
        if current_node not in visited:
          visited.add(current_node)

          edges = self.get_neighbors(current_node)

          # print('e', edges)
      
          for edge in edges:
            if edge not in visited:
              copyPath = current_path.copy()
              copyPath.append(edge)
              # copyPath.insert(0, edge)
              # print('c', copyPath)
              stack.push(copyPath)

              x = helper(edge)
              print(edge, x)
      # being wiped out by something.
      # print('again')

    helper(starting_vertex)

if __name__ == '__main__':
  graph = Graph()  # Instantiate your graph
  # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
  graph.add_vertex(1)
  graph.add_vertex(2)
  graph.add_vertex(3)
  graph.add_vertex(4)
  graph.add_vertex(5)
  graph.add_vertex(6)
  graph.add_vertex(7)
  graph.add_edge(5, 3)
  graph.add_edge(6, 3)
  graph.add_edge(7, 1)
  graph.add_edge(4, 7)
  graph.add_edge(1, 2)
  graph.add_edge(7, 6)
  graph.add_edge(2, 4)
  graph.add_edge(3, 5)
  graph.add_edge(2, 3)
  graph.add_edge(4, 6)

  '''
  Should print:
    {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
  '''
  print(graph.vertices)

  '''
  Valid BFT paths:
    1, 2, 3, 4, 5, 6, 7
    1, 2, 3, 4, 5, 7, 6
    1, 2, 3, 4, 6, 7, 5
    1, 2, 3, 4, 6, 5, 7
    1, 2, 3, 4, 7, 6, 5
    1, 2, 3, 4, 7, 5, 6
    1, 2, 4, 3, 5, 6, 7
    1, 2, 4, 3, 5, 7, 6
    1, 2, 4, 3, 6, 7, 5
    1, 2, 4, 3, 6, 5, 7
    1, 2, 4, 3, 7, 6, 5
    1, 2, 4, 3, 7, 5, 6
  '''
  graph.bft(1)

  '''
  Valid DFT paths:
    1, 2, 4, 7, 6, 3, 5
    1, 2, 3, 5, 4, 6, 7
    
    1, 2, 3, 5, 4, 7, 6
    1, 2, 4, 6, 3, 5, 7
  '''
    
  print('next')
  graph.dft(1)
  print('next1')
  graph.dft_recursive(1)

  '''
  Valid BFS path:
    [1, 2, 4, 6]
  '''
  print('next2')
  print(graph.bfs(1, 6))

  '''
  Valid DFS paths:
    [1, 2, 4, 6]
    [1, 2, 4, 7, 6]
  '''
  print('next3')
  print(graph.dfs(1, 6))
  # print('next4')
  # print(graph.dfs_recursive(1, 4))
