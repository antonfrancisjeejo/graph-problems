import sys

class Graph:
  def __init__(self,vertices):
    self.v=vertices
    self.graph=[[0 for columns in range(vertices)]for rows in range(vertices)]
  
  def minDistance(self,dist,visited):
    min=sys.maxsize
    min_index=0
    for i in range(self.v):
      if dist[i]<min and visited[i]==False:
        min=dist[i]
        min_index=i
    return min_index
  def dijkstra(self,source):
    dist=[sys.maxsize]*self.v
    dist[source]=0
    visited=[False]*self.v

    for i in range(self.v):
      u=self.minDistance(dist,visited)
      visited[u]=True
      for v in range(self.v):
        if self.graph[u][v]>0 and visited[v]==False and dist[u]+self.graph[u][v]<dist[v]:
          dist[v]=dist[u]+self.graph[u][v]

    self.printDistance(dist)
  def printDistance(self,dist):
    print("Vertex  Distance from source")
    for i in range(self.v):
      print("%d \t %d" %(i,dist[i]))

g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
		[4, 0, 8, 0, 0, 0, 0, 11, 0], 
		[0, 8, 0, 7, 0, 4, 0, 0, 2], 
		[0, 0, 7, 0, 9, 14, 0, 0, 0], 
		[0, 0, 0, 9, 0, 10, 0, 0, 0], 
		[0, 0, 4, 14, 10, 0, 2, 0, 0], 
		[0, 0, 0, 0, 0, 2, 0, 1, 6], 
		[8, 11, 0, 0, 0, 0, 1, 0, 7], 
		[0, 0, 2, 0, 0, 0, 6, 7, 0] 
		]; 

g.dijkstra(0); 

