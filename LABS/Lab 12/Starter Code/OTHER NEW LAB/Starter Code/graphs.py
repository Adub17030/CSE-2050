class Graph:
    def addVertex(self, vert):
        #Add a vertex with key k to the vertex set.
        raise NotImplemented

    def addEdge(self, fromVert, toVert):
        #Add a directed edge from u to v.
        raise NotImplemented

    def neighbors(self):
        #Return an iterable collection of the keys of all
        #vertices adjacent to the vertex with key v.
        raise NotImplemented

    def removeEdge(self, u, v):
        #Remove the edge from vertex u to v from graph.
        raise NotImplemented

    def removeVertex(self, v):
        #Remove the vertex v from the graph as well as any edges
        #incident to v.
        raise NotImplemented

    def __eq__(self, other):
        return set(self.edges()) == set(other.edges())
    
    ## Part 2
    # def dfsHelper(self, v):
    #     output = []
    #     for edge in self._E:
    #         if edge[0] == v:
    #             output.append(edge)
    #             x = self.dfsHelper(edge[1])
    #             output += x
    #     return output
    
    # def dfs(self, v):
    #     vList = self.dfsHelper(v)
    #     output = {}
    #     output[v] = None 
    #     for reachableVertex in vList:
    #         output[reachableVertex[1]] = reachableVertex[0]
    #     return output
    
    def dfs(self, v):
        tree = {}
        tovisit = [(None, v)]
        while tovisit:
            a,b = tovisit.pop()
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    tovisit.append((b,n))
        return tree

    
    def findPath(self, u, v):
        output = []
        paths = self.dfs(u)
        currentVertex = v
        while True:
            if v not in paths or u == v:
                return None
            if currentVertex is None:
                return None
            output.insert(0, currentVertex)
            if currentVertex is u:
                break
            currentVertex = paths[currentVertex]
        return output

        # for path in paths:
        #     if path[1] != v:
        #         output.append(path[1])
        #         x = self.findPath(path[1],v)
        #     else:
        #         break
        # if output[len(output)-1] != v:
        #     output = None
        # return output

class SimpleGraph(Graph):
    def __init__(self, V = None, E = None):
        self._V = set()
        self._E = set()
        if V is not None:
            for v in V: self.addVertex(v)
        if E is not None:
            for u,v,w in E: self.addEdge(u,v,w)
        self._nbrs = {}

    def wt(self, x, y):
        for u, v, w in self._E:
            if x == u and v == y:
                return w   

    def vertices(self):
        return iter(self._V)

    def edges(self):
        return iter(self._E)

    def addVertex(self, v):
        self._V.add(v)

    def addEdge(self, u, v, w):
        self._E.add((u, v, w))

    def neighbors(self, v):
        return (w for u, w in self._E if u == v)

    def removeEdge(self, u, v, w):
        self._E.remove((u, v, w))

    def removeVertex(self, v):
        for neighbor in list(self.neighbors(v)):
            self.removeEdge(v, neighbor)
        self._V.remove(v)

    def nbrs(self, v):
        return (w for u,w in self._E if u == v)

## Part 1
class SimpleUGraph(SimpleGraph):
    def addEdge(self, u, v, w=None):
        self._E.add((u,v,w))
        self._E.add((v,u,w))

    def removeEdge(self, u, v, w=None):
        self._E.remove((u,v,w))
        self._E.remove((v,u,w))

## Part 3
class AdjacencyListGraph(SimpleGraph):
    def __init__(self, V, E):
        self._V = set()
        self._E = set()
        self._neighbors = {}
        for v in V: self.addVertex(v)
        for u,v in E: self.addEdge(u,v)

    def addEdge(self, u, v):
        self._E.add((u,v))
        if u in self._neighbors:
            self._neighbors[u].append(v)
        else:
            self._neighbors[u] = []
            self._neighbors[u].append(v)

    def removeEdge(self, u, v):
        self._E.remove((u, v))

class AdjacencyListUGraph(AdjacencyListGraph):
    def addEdge(self, u, v):
        self._E.add((u,v))
        self._E.add((v,u))
        if u in self._neighbors:
            self._neighbors[u].append(v)
        else:
            self._neighbors[u] = []
            self._neighbors[u].append(v)

        # self._E.add((v,u))
        # if u in self._neighbors:
        #     self._neighbors[v].append(u)
        # else:
        #     self._neighbors[v] = []
        #     self._neighbors[v].append(u)

    def removeEdge(self, u, v):
        self._E.remove((u, v))
        self._E.remove((v, u))

## Part 4
class AdjacencyMatrixGraph(SimpleGraph):
    def __init__(self, V, E):
        self._V = set()
        self._E = set()
        self._neighbors = []
        for v in V: self.addVertex(v)
        for u,v in E: self.addEdge(u,v)
        for index in range(len(V)):
            self._neighbors.append([])
            for innerIndex in range(len(V)):
                self._neighbors[index].append(0)
            
        
    def addEdge(self, u, v):
        self._E.add((u,v))
    
    def removeEdge(self, u, v):
        self._E.remove((u, v))

class AdjacencyMatrixUGraph(AdjacencyMatrixGraph):
    def addEdge(self, u, v):
        self._E.add((u,v))
        self._E.add((v,u))
    
    def removeEdge(self, u, v):
        self._E.remove((u, v))
        self._E.remove((v, u))
        


# g1 = SimpleGraph({1,2,3,4}, {(1,2), (1,4), (2,3)})
# print(list(g1.vertices()))
# print(list(g1.edges()))
# g1.removeVertex(1)
# print(list(g1.vertices()))
# print(list(g1.edges()))

# print("--------------------")

# g1 = SimpleUGraph({1,2,3,4}, {(1,2), (1,4), (2,3)})
# print(list(g1.vertices()))
# print(list(g1.edges()))
# g1.removeVertex(1)
# print(list(g1.vertices()))
# print(list(g1.edges()))

# G = SimpleGraph({'A','B','C','D','E'}, {('A','B'), ('A','C'), ('B','E'),
# ('E','D'), ('D', 'T'), ('A', 'Z')})
# t = G.dfs('A')
# print(t)
# print(G.findPath('A', 'D'))

# G = SimpleGraph({'1','2','3','4','5'}, {('1','2'), ('1','4'), ('2','3'),
# ('3','5'), ('3', '4')})
# t = G.dfs('1')
# p = G.findPath('1', '3')
# print(t)
# print(p)