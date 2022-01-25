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
    
    bfs(graph, 2, callback = lambda v: print(v,end = ' '))
    print()
    dfs(graph, 2, callback = lambda v: print(v,end = ' '))
    print()
    print(hasCycle(graph))
    
    
    graph = Graph()
    graph[0] = GraphNode(0)
    graph[1] = GraphNode(1)
    graph[2] = GraphNode(2)
    graph[3] = GraphNode(3)
    graph[9] = GraphNode(9)
    
    graph[0].addEdge(graph[1],directed = False)
    graph[1].addEdge(graph[3],directed = False)
    #graph[2].addEdge(graph[3],directed = False)
    graph[2].addEdge(graph[0],directed = False)
    graph.printGraph()
    print(hasCycle(graph))
    
    arr = [PriorityElement((1,1)),PriorityElement((2,2)),PriorityElement((3,3)),PriorityElement((4,4)),PriorityElement((5,5)),PriorityElement((6,6)),PriorityElement((7,7)),PriorityElement((8,8))]
    heap = NAryMinHeap(3,arr)
    print(heap.top())
    print(heap.pop())
    print(heap)
    heap = MinHeap(arr)
    print(heap)

    
