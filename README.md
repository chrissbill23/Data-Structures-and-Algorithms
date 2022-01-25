# Data-Structures-and-Algorithms
My implementations in Python of some Data Structures and Algorithms.

##  Data structures implemented
* [Heaps](./DataStructures/Heap.py)
* [Priority Heaps](./DataStructures/Heap.py) same as the heaps but containing data if a form (key,value).
* [N-ary Heaps](./DataStructures/Heap.py) are heaps where each node has at most n children. It is used when we want a smaller height of the tree in order to reduce the lookup time.
* [Queue](./DataStructures/Queue.py) with O(1) enqueue and O(1) dequeue operations
* [Priority Queue](./DataStructures/Queue.py) provided intervafe for concrete implementation like the priority heaps. It has multiple applications on CPU scheduling, Graphs algorithms, Data compression, etc.
* [Graph](./DataStructures/Graph.py): Ajacency list and Object-pointers representation

## Algorithms implemented

### [Maths](./Algorithms/Maths.py)
* [Binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient) O(n) in time, O(1) in space
* [Catalan numbers](https://brilliant.org/wiki/catalan-numbers/) O(n) in time and O(1) in space
### [Graph Algorithms](./Algorithms/GraphAlgorithms.py)
* [BFS (Breadth First Search traversal)](https://en.wikipedia.org/wiki/Breadth-first_search) : with callback on the traversed node.
* [DFS (Depth First Search traversal)](https://en.wikipedia.org/wiki/Depth-first_search) : with callback on the traversed node.
* [Cycle detection](https://en.wikipedia.org/wiki/Cycle_(graph_theory)#:~:text=real%20numbers%2C%20etc.-,Cycle%20detection,over%20are%20part%20of%20cycles.) in directed and undirected graphs
### [Heap Algorithms](./Algorithms/HeapAlgorithms.py)
* [Kth largest element](https://www.baeldung.com/java-kth-largest-element#:~:text=To%20find%20the%20kth%20largest%20element%2C%20we%20can%20pass%20k,length(Array)%20%E2%80%93%20k.&text=Now%20let's%20implement%20the%20partition,less%20than%20the%20pivot%20element.) using heap.
