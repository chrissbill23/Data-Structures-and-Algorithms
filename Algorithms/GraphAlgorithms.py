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
