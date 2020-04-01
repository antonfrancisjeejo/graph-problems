import sys
class Graph:
  def __init__(self,vertices):
    self.v=vertices
    self.graph=[[0 for columns in range(vertices)]for row in range(vertices)]

  def minDistance(self,visited_weights,visited):
    min=sys.maxsize
    for i in range(self.v):
      if visited_weights[i]<min and visited[i]==False:
        min=visited_weights[i]
        min_index=i
    return min_index

  def printTree(self, current_tree):
    total_cost=0 
    print("Edge \tWeight")
    for i in range(1, self.v): 
      print(current_tree[i], "-", i, "\t", self.graph[i][ current_tree[i] ] )
      total_cost+=self.graph[i][current_tree[i]]
    print("Total cost: %d"%total_cost)
#   Select a minimum which is connected to either any of the initial vertices 
  def primMST(self): 
    visited_weights = [sys.maxsize] * self.v 
    current_tree = [None] * self.v
    visited_weights[0] = 0
    visited = [False] * self.v
    current_tree[0] = -1 
    for cout in range(self.v): 
      u = self.minDistance(visited_weights, visited) 
      visited[u] = True
      for v in range(self.v): 
        if self.graph[u][v] > 0 and visited[v] == False and visited_weights[v] > self.graph[u][v]: 
            visited_weights[v] = self.graph[u][v] 
            current_tree[v] = u 
    self.printTree(current_tree)

g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
			[2, 0, 3, 8, 5], 
			[0, 3, 0, 0, 7], 
			[6, 8, 0, 0, 9], 
			[0, 5, 7, 9, 0]] 

g.primMST(); 
