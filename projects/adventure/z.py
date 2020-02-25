# x = True

# while x == True:
#   print('hi')

#   for i in range(1,10):
#     if i % 2 == 0:
#       print(i)
#       break

  # print('bye')

graph = {0: {'n': 1, 's': 5, 'w': 7, 'e': '?'}, 7: {'w': 8, 'e': 0}, 8: {'s': 9, 'e': 7}, 9: {'n': 8, 's': 10}, 10: {'n': 9, 'e': 11}, 11: {'w': 10, 'e': 6}, 6: {'n': 5, 'w': 11}, 5: {'n': 0, 's': 6}, 1: {'n': 2, 's': 0, 'w': 15, 'e': 12}, 2: {'s': 1}, 15: {'w': 16, 'e': 1}, 16: {'n': 17, 'e': 15}, 17: {'s': 16}, 12: {'w': 1, 'e': 13}, 13: {'n': 14, 'w': 12}, 14: {'s': 13}}

current_node = 1

for dr in graph[current_node]:
	# print(graph[current_node][dr], graph[graph[current_node][dr]])
	if '?' in graph[graph[current_node][dr]].values():
		print(dr, graph[current_node][dr])
	# print(dr)