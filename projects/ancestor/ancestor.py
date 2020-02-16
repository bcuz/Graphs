
from util import Stack, Queue  # These may come in handy
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
  # seems like depth first
  # planning just seems like procrastination, mayne
  # always go in the direction of the lower number when there's a fork in the road
  # something about when the last one is reached in the longest branch, return the last node and stop traversing
  # can just try and solve first, worry about proper structure after (helper fcs, so on)

  # 1 - 11
  graph = Graph()  
  allNodes = []

  # loop to add each vertex
  for tup in ancestors:
    if tup[0] not in allNodes:
      allNodes.append(tup[0])
      graph.add_vertex(tup[0])
    if tup[1] not in allNodes:
      allNodes.append(tup[1])
      graph.add_vertex(tup[1])    

  # loop to add edges
  for tup in ancestors:
    # print(tup[1], tup[0])
    graph.add_edge(tup[1], tup[0])

  # add both ways? or maybe add the edges in opposite.
  # print(graph.get_neighbors(2))
  # it pops from the end of edges
  # print(graph.dft(1))
  return graph.dfs(starting_node)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 8))