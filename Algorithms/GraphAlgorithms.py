from DataStructures import Graph, GraphNode, Queue

def bfs(graph: Graph, s_key = None, callback = None):
    # time O(V+E), space O(2*V)
    visited = set()
    queue = Queue()
    
    def traversal(v):
        nonlocal queue
        nonlocal visited
        queue.append(v.key)
        while not(queue.isEmpty()):
            n = graph[queue.pop()]
            if n.key not in visited:
                visited.add(n.key)
                if callback is not None:
                    callback(n)
                for e in n.edges:
                    if e.tov.key not in visited:
                        queue.append(e.tov.key)
    if s_key is not None:
        traversal(graph[s_key])
    for v in graph:
        traversal(v)

def dfs(graph: Graph, s_key = None, callback = None):
    # time O(V+E), space O(V)
    visited = set()
    stack = []
    
    def traversal(v):
        nonlocal stack
        nonlocal visited
        stack.append(v.key)
        while len(stack) > 0:
            key = stack.pop()
            if key not in visited:
                n = graph[key]
                visited.add(key)
                if callback is not None:
                    callback(n)
                for e in n.edges:
                    if e.tov.key not in visited:
                        stack.append(e.tov.key)
    if s_key is not None:
        traversal(graph[s_key])
    for v in graph:
        traversal(v)
        
def hasCycle(graph: Graph)->bool:
    # time O(V+E), space O(V)
    visited = set()
    
    def helper(v, parent):
        nonlocal visited
        visited.add(v.key)
        for e in v.edges:
            if e.tov.key not in visited: 
                if helper(e.tov,v):
                    return True
            elif parent is not None and e.tov.key != parent.key:
                return True
        return False
    for v in graph:
        if v.key not in visited:
            if helper(v, None) == True:
                return True
    return False
    
    