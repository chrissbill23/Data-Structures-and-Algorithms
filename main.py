from DataStructures import *
from Algorithms import *


if __name__ == "__main__":
    graph = Graph()
    graph[0] = GraphNode(0)
    graph[1] = GraphNode(1)
    graph[2] = GraphNode(2)
    graph[3] = GraphNode(3)
    graph[9] = GraphNode(9)
    
    graph[0].addEdge(graph[1])
    graph[0].addEdge(graph[2])
    graph[1].addEdge(graph[2])
    graph[2].addEdge(graph[0])
    graph[2].addEdge(graph[3])
    graph[3].addEdge(graph[3])
    
    graph.printGraph()
    
    bfs(graph, callback = lambda v: print(v,end = ' '))
    print()
    dfs(graph, callback = lambda v: print(v,end = ' '))
