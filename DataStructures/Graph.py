
# Graph: Object-pointers representation and Adjacency list representation
# Space complexity: O (V+2E) in non-directed graph and O(V+E) in di-graphs
# Time complexity: O(1) for insertion and deletion of vertices and edges

class GraphNode:
    
    def __init__(self, data=None, keys=None):
        self.__key = keys or id(self)
        self.__data = data
        self.__edges = set()
        
    def __str__(self):
        return str(self.__key)
        
    def __hash__(self):
        return hash((self.__key,self.__data))
        
    def __eq__(self, other):
        if not isinstance(other, type(self)): 
            return False
        return self.__key == other.__key and self.__data == other.__data
        
    def addEdge(self, dest, weight = 1, directed = True):
        e = GraphEdge(self,dest,weight,directed)
        self.__edges.add(e)
        if directed == False:
            dest.__edges.add(GraphEdge(dest,self,weight,directed))
    def removeEdge(self, dest, weight = 1, directed = True):
        self.__edges.discard(GraphEdge(self,dest,weight))
        if not(directed):
            dest.__edges.discard(GraphEdge(dest,self,weight,directed))
        
    @property
    def edges(self):
        return self.__edges
    
    @property
    def key(self):
        return self.__key
        
    @key.setter
    def key(self, k):
        self.__key = k
        
    def hasEdge(self,dest):
        return GraphEdge(self,dest) in self.__edges
        
class GraphEdge:
    
    def __init__(self, start: GraphNode, end: GraphNode, weight = 1, directed = True):
        self.fromv = start
        self.tov = end
        self.weight = weight
        self.__di = directed
        
    @property
    def directed(self):
        return self.__di
        
    def __hash__(self):
        return hash((self.fromv, self.tov))
        
    def __eq__(self, other):
        if not isinstance(other, type(self)): 
            return False
        return self.fromv == other.fromv and self.tov == other.tov and self.weight == other.weight
        
class Graph:
    
    def __init__(self, vertices = None):
        # O(len(vertices))
        self.__nodes = {}
        if vertices is not None:
            for v in vertices:
                self.__nodes[v] = v
                
    def addNode(self, v: GraphNode):
        # O(1)
        self.__nodes[v] = v
        
    def removeNode(self, key):
        # O(1)
        if key in self.__nodes:
            del self.__nodes[key]
            
    def removeNode(self, v: GraphNode):
        # O(1)
        self.removeNode(v.key)
        
    def printGraph(self):
        # O(V + E)
        for v in self:
            print(v, end='--->(')
            for e in v.edges:
                print(e.tov, end=',')
            print(')')
            
    @property
    def vertices(self):
        return self.__nodes.values()
        
    @property     
    def keys(self):
        return self.__nodes.keys()
        
    def __str__(self):
        return str(self.__nodes)
        
    def __repr__(self):
        return self.__str__()
        
    def __contains__(self, item):
        # O(1)
        return item in self.__nodes
        
    def __iter__(self):
        # O(1)
        return iter(self.__nodes.values())
    
    def __len__(self):
        # O(1)
        return len(self.__nodes)
    
    def __getitem__(self, key):
        # O(1)
        if key in self.__nodes:
            return self.__nodes[key]
        return None
        
    def __setitem__(self, key, v: GraphNode):
        # O(1)
        if key != v.key:
            v.key = key
        self.__nodes[key] = v
            

