from graphs import *

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

def dfs(G, v):
    tree = {}
    tovisit = [(None, v)]
    while tovisit:
        a,b = tovisit.pop()
        if b not in tree:
            tree[b] = a
            for n in G.nbrs(b):
                tovisit.append((b,n))
    return tree



def findPath(G, u, v):
    output = []
    paths = dfs(G, u)
    currentVertex = v
    while True:
        if v not in paths:
            return None
        if currentVertex is None:
            return None
        output.insert(0, currentVertex)
        #print(output)
        if currentVertex is u:
            break
        currentVertex = paths[currentVertex]
    return output

def KBNcompute(G, A):
  if A == 'Bacon, Kevin':
    return 0
  x = findPath(G, 'Bacon, Kevin', A)
  if x == None:
    return float('inf')
  else:
    return 1



# mapAtoM = getMapAtoM()
# #print (mapAtoM['Rock, Chris']) # the set of Chris Rock's movies
# G = createActorGraph(mapAtoM)
# print ('Bacon, Kevin' in G.neighbors('Costner, Kevin')) # should print True
# k = KBNcompute(G, 'Coestner, Kevin') # should return 1
# print(k)
