from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

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

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

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

while stack.size() > 0:
  currentRoom = stack.pop()
  print(currentRoom)

  if currentRoom not in graph:
    graph[currentRoom] = {}

    for direction in player.current_room.get_exits():
      graph[player.current_room.id][direction] = '?'

    # think i need to do more w/ not picking an exit that takes me to prev room
    # way it's set up the random direction is always going north from the first if statement below
    randomExitIndex = random.randint(0, len(player.current_room.get_exits())-1)
    if len(graph) == 1:
      randomDirection = player.current_room.get_exits()[randomExitIndex]
    else:
      print(graph)
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
        continue
      else:
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

print(graph)
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
