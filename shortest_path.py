# Gyan Suri, gs675
# Ryan Gale

# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError
import heapq

def shortest_path(graph, source, target):
  # `graph` is an object that provides a get_neighbors(node) method that returns
  # a list of (node, weight) edges. both of your graph implementations should be
  # valid inputs. you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  # 
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  #
  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  #
  # NOTE: Please see instructions.txt for additional information about the
  # return value of this method.

  # TODO: YOUR CODE HERE, delete the `raise NotImplementedError`line below once you finish writing your code
  
  #Priority_Q keeps track of which node to visit next
  priority_q = [] 
  heapq.heappush(priority_q, (0, source))
  #visited dict keeps track of which nodes have been visited
  visited = set()
  #For any given node, path will store previous node we came from
  path = {source: None}
  #Remaining, for bookeeping purposes, stores Nodes and current value of path
  remaining = dict()
  while(priority_q):
    visting_node = heapq.heappop(priority_q)
    curr_path_weight = visting_node[0]
    curr_node = visting_node[1]
    if curr_node in visited:
      continue
    elif curr_node == target:
      print(get_path(source, curr_node, path))
      return (get_path(source, curr_node, path), curr_path_weight)
    for neighbor, edge_weight in graph.get_neighbors(curr_node):
      if neighbor not in visited and (neighbor not in remaining or remaining[neighbor] > curr_path_weight+edge_weight):
        remaining[neighbor] = curr_path_weight + edge_weight
        path[neighbor] = curr_node
        heapq.heappush(priority_q, (remaining[neighbor], neighbor))
    visited.add(curr_node)
  return None


def get_path(source, target, path_dict):
  result = list()
  node = target
  while node != None:
    result.append(node)
    node = path_dict[node]
  return result
