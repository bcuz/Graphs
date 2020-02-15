
from util import Stack, Queue  # These may come in handy
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
  # seems like depth first
  # always go in the direction of the lower number when there's a fork in the road
  # something about when the last one is reached in the longest branch, return the last node and stop traversing
  # can just try and solve first, worry about proper structure after (helper fcs, so on)

  # 1 - 11
  
  x = []

  for tup in ancestors:
    for vl in tup:
      if vl not in x:
        x.append(vl)


  x.sort()
  print(x)




