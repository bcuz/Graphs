from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()
# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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


# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
traversal_path = ['n', 'e', 'w', 'n']
traversal_path = []

stack = Stack()
# visited = set()
graph = {}
lastDir = {'dir': None, 'roomNum': None}
oppositeDir = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

stack.push(player.current_room.id)

# create with all exits of room 0
# {0: {'n': '?'}}
# move north. note that we came from the north (last item in path)
# how do we get the id of the last room? when we cant check what's behind a door?
# {
#  0: {'n': '1'}, 
#  1: { 's': 0, 'n': '?'}
# }
elseState = None

while stack.size() > 0:
  currentRoom = stack.pop()
  print(currentRoom)

  # it should go here
  if currentRoom not in graph or elseState == True:
    elseState = False
    graph[currentRoom] = {}

    for direction in player.current_room.get_exits():
      graph[player.current_room.id][direction] = '?'

    # think i need to do more w/ not picking an exit that takes me to prev room
    # way it's set up the random direction is always going north from the first if statement below
    randomExitIndex = random.randint(0, len(player.current_room.get_exits())-1)
    if len(graph) == 1:
      # move line up and make general area more concise. if != 1 do something
      # so there wouldnt be an else
      randomDirection = player.current_room.get_exits()[randomExitIndex]
    else:
      # print(graph)
      randomDirection = player.current_room.get_exits()[randomExitIndex]      
      # what if it's a dead end? check for a certain thing being in the lastDir, and the
      # length of the exits. something along those lines. this feels super messy...
      # use later
      # if player.current_room.get_exits()[randomExitIndex] == oppositeDir[lastDir['dir']] and 
      if len(player.current_room.get_exits()) == 1:
        # updating graph with current room info.

        # this could be where i have to backtrack
        graph[player.current_room.id][oppositeDir[lastDir['dir']]] = lastDir['roomNum']
        graph[lastDir['roomNum']][lastDir['dir']] = player.current_room.id

        # bfs to nearest question mark
        # then make a move based on that data. hazy at this point
        # go opposite direction until there is a ? found
        print(graph, player.current_room.id)

        count = 0
        # if there are no '?' in the entire graph, break from the loop?
        for item in graph:
          # print(item)
          for dr in graph[item]:
            if graph[item][dr] == '?':
              count += 1

        if count == 0:
          break

        queue = Queue()
        visited = set()
        path = [player.current_room.id]

        queue.enqueue(path)

        while queue.size() > 0:
          current_path = queue.dequeue() 
          current_node = current_path[-1] 
          # print('c', current_node)

          print('x', current_path, graph[current_node].values())

          if '?' in graph[current_node].values():
            # then we need to take the item in this var
            # and start dft again on any of the q marks.
            ans = current_path

            # traversing the path once you get it.
            print('a', ans)
            stack.push(ans[-1])  
            # print(5, ans)
            break
          else:
            if current_node not in visited:
              visited.add(current_node)

              # print('z', current_node, graph[current_node])
              # print('c', current_node, len(graph[current_node]), graph[current_node])

              # if there's only one way to go back, take that way.
              if len(graph[current_node]) == 1:
                dirTravel = list(graph[current_node].keys())[0]
                player.travel(dirTravel)

                traversal_path.append(dirTravel)

                lastDir['dir'] = dirTravel
                lastDir['roomNum'] = current_node

              else:
                # print('c', current_node, lastDir)
                # cant go the opposite of the last direction.
                # maybe a break after moving in this loop
                # print('y', player.current_room.id, current_node)

                # probably shouldnt be relying on randomess here. should be building
                # something to the next ? space

                randomExitIndex = random.randint(0, len(player.current_room.get_exits())-1)                        
                randomDirection = player.current_room.get_exits()[randomExitIndex]                 

                while randomDirection == oppositeDir[lastDir['dir']]:
                  randomExitIndex = random.randint(0, len(player.current_room.get_exits())-1)          
                  randomDirection = player.current_room.get_exits()[randomExitIndex]   

                player.travel(randomDirection)

                traversal_path.append(randomDirection)

                lastDir['dir'] = randomDirection
                lastDir['roomNum'] = current_node

                # for direct in graph[current_node]:
                #   # if we've never traveled there. 

                #   # should include randomness here. not sure that will solve
                #   # things but it might make things pass sometimes. prob wont make the bigger
                #   # graph solve

                #   if direct != oppositeDir[lastDir['dir']]:
                #     player.travel(direct)

                #     traversal_path.append(direct)

                #     lastDir['dir'] = direct
                #     lastDir['roomNum'] = current_node                    
                #     break

              # print('h', player.current_room.id)

              # edges = self.get_neighbors(current_node)
              # print(edges)

              copyPath = current_path.copy()
              copyPath.append(player.current_room.id)
              # print(copyPath)
              # path.append(copyPath)
              queue.enqueue(copyPath)

              # not sure if below needed
              # for edge in edges:
              #   if edge not in visited:
              #     copyPath = current_path.copy()
              #     copyPath.append(edge)
              #     # print(copyPath)
              #     # path.append(copyPath)
              #     queue.enqueue(copyPath)

        # print(ans)
        # print(traversal_path)


        continue
      else:

        # keep regenerating a random direction until we get any room 
        # EXCEPT the one we came from
        # print('h', currentRoom)
        while randomDirection == oppositeDir[lastDir['dir']]:
          randomExitIndex = random.randint(0, len(player.current_room.get_exits())-1)          
          randomDirection = player.current_room.get_exits()[randomExitIndex]      

        graph[player.current_room.id][oppositeDir[lastDir['dir']]] = lastDir['roomNum']
        graph[lastDir['roomNum']][lastDir['dir']] = player.current_room.id

      
    # this is in progress:
    # will need to check that we're not moving somewhere we've already moved
    # on the second loop around. if statement.

    # what if im going from dead end to new branch of the dft?
    lastDir['dir'] = randomDirection
    lastDir['roomNum'] = currentRoom

    player.travel(randomDirection)
    traversal_path.append(randomDirection)

    stack.push(player.current_room.id)  
    # 0 is being added to the stack.
    # print('w', stack.stack)
  else:

    graph[player.current_room.id][oppositeDir[lastDir['dir']]] = lastDir['roomNum']
    graph[lastDir['roomNum']][lastDir['dir']] = player.current_room.id

    print('c', currentRoom, graph[currentRoom])

    # something happening when we got back to 0. not adding to stack?

    if '?' not in graph[currentRoom].values():
      break
    else:
      for direct in graph[currentRoom]:
        if graph[currentRoom][direct] == '?':

          player.travel(direct)
          traversal_path.append(direct)

          # make the move, record it, then let the while do the rest
          # not that easy
          graph[player.current_room.id] = {}

          for direction in player.current_room.get_exits():
            graph[player.current_room.id][direction] = '?'

          # not here because the loop might take care of it on the next go around
          # graph[player.current_room.id][oppositeDir[lastDir['dir']]] = lastDir['roomNum']
          # graph[lastDir['roomNum']][lastDir['dir']] = player.current_room.id

          lastDir['dir'] = direct
          lastDir['roomNum'] = currentRoom

          # need it to revert back to the main logic for things to work. so things go back to breadth
          # could try a variable.

          # print('s', currentRoom, graph[currentRoom])
          # not recording it on the graph
          # maybe need last direction stuff here, too

          # print('hi')
          stack.push(player.current_room.id)  
          elseState = True
          break


# print(graph)
print(traversal_path)
# add current room to tgraph
# need to loop and put all possible exits for it
# move a random direction, but need to keep track of where i came from.
# object with last room num and !last_direction?


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
