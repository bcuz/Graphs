
def earliest_ancestor(ancestors, starting_node):
  
  # cuz we only search parents. 
  # essentially the get neighbors part of the problem
  def getParents(child):
    parents = []

    for tup in ancestors:
      if tup[1] == child:
        parents.append(tup[0])

    print(parents)

  getParents(starting_node)

  # if it doesnt have parents, return -1

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 3)