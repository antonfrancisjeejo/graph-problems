graph ={ 
'a':['c'], 
'b':['d'], 
'c':['e'], 
'd':['a', 'd'], 
'e':['b', 'c'] 
}
def find_path(graph,start,end,path=[]):
  path.append(start)
  if start==end:
    return path
  for node in graph[start]:
    if node not in path:
      new_path=find_path(graph,node,end,path)
      if new_path:
        return new_path
      return None
print(find_path(graph,'a','d'))
