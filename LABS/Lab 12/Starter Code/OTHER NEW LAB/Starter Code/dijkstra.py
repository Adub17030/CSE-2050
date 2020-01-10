import math
from graphs import *


class PQ:
  def __init__(self):
    self._L = []
  def insert(self, item, priority):
    self._L.append((item, priority))
  def findmin(self):
    return min(self._L, key = lambda x : x[1])[0]
  def removemin(self):
    item, priority = min(self._L, key = lambda x : x[1])
    self._L.remove((item, priority))
    return item
  def reducepriority(self,n, m):
    for k in range(len(self._L)):
      if self._L[k][0] == n:
        self._L[k] = (n,m)
  def __len__(self):
    return len(self._L)


def getMapAtoM():
  fp = open("lg_actor_data.txt", "r") 
  mapAtoM = {}
  for s in fp:
    if not s.strip():
      continue
  
    #print(s)
    l1 = s.split("\t")
    if s[0].isalpha():
      actor = l1[0].split("(")[0].strip()
    movie = l1[-1].split(")")[0].strip() + ')'
    #print ("ACTOR:",actor)
    #print("MOVIE:", movie)  

    if actor not in mapAtoM:
      mapAtoM[actor] = set([movie]) 
    elif movie not in mapAtoM[actor]:
      mapAtoM[actor].add(movie)

  fp.close()
  return mapAtoM

## Use the SimpleUGraph from the previous lab

def createActorGraph(mapAtoM):
  G = SimpleUGraph()

  for actor in mapAtoM.keys():
    G.addVertex(actor) 

  for actor in mapAtoM.keys():
    for innerActor in mapAtoM.keys():
      if actor != innerActor:
        if not mapAtoM[actor].isdisjoint(mapAtoM[innerActor]):
          G.addEdge(actor, innerActor)
  
  return G

def Dijkstra(G, initial):
  ## Write your code here
  tree = {initial: None}
  D = {u: float('inf') for u in G.vertices()}
  D[initial] = 0
  tovisit = PQ()
  for u in G.vertices():
    tovisit.insert(u, D[u])
  while len(tovisit)!=0:
    u = tovisit.removemin()
    for n in G.neighbors(u):
      if D[u] + G.wt(u, n) < D[n]:
        D[n] = D[u] + G.wt(u, n)
        tree[n] = u
        tovisit.reducepriority(n, D[n])
  return tree, D

## Use getPath() function fro previous lab

# mapAtoM = getMapAtoM()
# G = createActorGraph(mapAtoM)
# paths = Dijkstra(G, 'Bacon, Kevin')
# path1 = getPath(G, paths, 'Weaver, Jason')
# for x in path1[::-1]:
#   print(x)
# # path2 = getPath(G, paths, 'Costner, Kevin')
# # for x in path2[::-1]:
# #   print(x)
# # path3 = getPath(G, paths, 'Pesci, Joe')
# # for x in path3[::-1]:
# #   print(x)


