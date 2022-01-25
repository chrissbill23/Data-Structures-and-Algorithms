# HEAP module:Heap (Base abstract class); Minheap and Maxheap concrete classes; 
# NAryHeap: base abstract class of N-ary heap trees; NAryMinHeap and NAryMaxHeap concrete classes
# PriorityHeap: base of priority heaps

from .Queue import PriorityQueue, PriorityElement

class Heap :
    def __init__(self, heap = []):
        self.__values = heap
        
    def getNodes(self):
        return self.__values
    
    def hasParent(self, index):
        return 0 <= (index - 1) // 2  < len(self.__values)
    
    def parent(self, index):
        return (index - 1) // 2
    
    def hasLeftChild(self, index):
        return 0 <= 2*index + 1 < len(self.__values)
    
    def hasRightChild(self, index):
        return 0 <= 2*index + 2 < len(self.__values)
    
    def rightChild(self, index):
        r = 2*index + 2
        if r >= len(self.__values):
            raise ValueError('The node given has not a right child')
        return r
    
    def leftChild(self, index):
        l = 2*index + 1
        if l >= len(self.__values):
            raise ValueError('The node given has not a left child')
        return l
    
    def compare(self, mainindex, otherindex):
        raise NotImplementedError()
        
    def getBestIndex(self,*indexes):
        best = indexes[0]
        for i in range(1,len(indexes)):
            if self.compare(indexes[i], best):
                best = indexes[i]
        return best
        
    def getChildrenIndex(self, index):
        all_children = []
        if self.hasLeftChild(index):
            all_children.append(self.leftChild(index))
        if self.hasRightChild(index):
            all_children.append(self.rightChild(index))
        return all_children   
        
    def heapifyUp(self, index):
        while self.hasParent(index) and self.compare(index, self.parent(index)):
            newind = self.parent(index)
            self.__values[newind], self.__values[index] = self.__values[index], self.__values[newind]
            index = newind
            
    def heapifyDown(self, index):
        while self.hasLeftChild(index):
            newind = index 
            if self.compare(self.leftChild(index), newind):
                newind = self.leftChild(index)
            if self.hasRightChild(index) and self.compare(self.rightChild(index), newind):
                newind = self.rightChild(index)
            if newind == index:
                break
            self.__values[index], self.__values[newind] = self.__values[newind], self.__values[index]
            index = newind
        
    def addNode(self, value):
        self.__values.append(value)
        self.heapifyUp(len(self.__values)-1)
        
    def removeNode(self, index):
        if len(self.__values) == 0:
            raise ValueError('The tree is empty')
        if index >= len(self.__values):
            raise ValueError('The node given is not in the tree')
        val = self.__values[index]
        self.__values[index] = self.__values[len(self.__values)-1] 
        self.__values.pop()
        self.heapifyDown(index)
        return val
    
    def  poll(self):
        return self.removeNode(len(self.__values)-1)
    
    def  peek(self):
        return self.removeNode(0)
    
    def __printHelper(self, currind):
        # BFS printing
        nodes = self.getNodes()
        s = ''
        children = [currind]
        while len(children) > 0:
            currind = children.pop(0)
            tmp = self.getChildrenIndex(currind)
            s += str(nodes[currind])+'-->(' + ','.join([ str(nodes[c]) for c in tmp])+')\n'
            children += tmp 
        return s
    
    def __str__(self):
        return self.__printHelper(0) 
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.__values)
    
    def __getitem__(self, key):
        return self.__values[key]

class PriorityHeap(Heap,PriorityQueue):
    def __init__(self, heap = []):
        Heap.__init__(self, heap)
        
    def append(self, value: PriorityElement):
        self.addNode(value)
        
    def top(self)->PriorityElement:
        if self.isEmpty():
            raise ValueError('Heap is empty')
        return self.getNodes()[0]
        
    def pop(self)->PriorityElement:
        return self.peek()   
        
        

class MinHeap(PriorityHeap):
    def compare(self, mainindex, otherindex):
        nodes = self.getNodes()
        return nodes[mainindex] < nodes[otherindex]
        
class MaxHeap(PriorityHeap):
    def compare(self, mainindex, otherindex):
        nodes = self.getNodes()
        return nodes[mainindex] > nodes[otherindex]
 
 
       
class NAryHeap(Heap):
    def __init__(self,n, heap = []):
        super().__init__( heap)
        self.__n = n if n > 2 else 3
    
    def hasParent(self, index):
        return 0 <= (index - 1) // self.__n  < len(self.getNodes())
    
    def parent(self, index):
        return (index - 1) // self.__n
    
    def hasLeftChild(self, index):
        return 0 <= self.__n*index + 1 < len(self.getNodes())
    
    def hasRightChild(self, index):
        return 0 <= self.__n*index + 2 < len(self.getNodes())
    
    def hasNthChild(self, index,n):
        return n > 0 and 0 <= self.__n*index + n < len(self.getNodes())
        
    def getNthChild(self, index,n):
        r = self.__n*index + n
        if r >= len(self.getNodes()):
            raise ValueError('The node given has not a right child')
        return r
        
    def getChildrenIndex(self, index):
        all_children = []
        tot = len(self.getNodes())
        for i in range(1, self.__n+1):
            if 0 <= self.__n*index + i < tot:
                all_children.append(self.__n*index + i)
            else:
                break
        return all_children
        
    def rightChild(self, index):
        r = self.__n*index + 2
        if r >= len(self.getNodes()):
            raise ValueError('The node given has not a right child')
        return r
    
    def leftChild(self, index):
        l = self.__n*index + 1
        if l >= len(self.getNodes()):
            raise ValueError('The node given has not a left child')
        return l
            
    def heapifyDown(self, index):
        children = self.getChildrenIndex(index)
        nodes = self.getNodes()
        while len(children) > 0:
            children[0:0] = [index]
            newind = self.getBestIndex(*children)
            if newind == index:
                break
            nodes[index], nodes[newind] = nodes[newind], nodes[index]
            index = newind
            children = self.getChildrenIndex(index)

 
    
class NAryMinHeap(NAryHeap, PriorityHeap):
    def __init__(self,n,heap=[]):
        NAryHeap.__init__(self, n,heap)
    def compare(self, mainindex, otherindex):
        nodes = self.getNodes()
        return nodes[mainindex] < nodes[otherindex]
        
        
class NAryMaxHeap(NAryHeap, PriorityHeap):
    def __init__(self,n,heap=[]):
        NAryHeap.__init__(self, n,heap)
    def compare(self, mainindex, otherindex):
        nodes = self.getNodes()
        return nodes[mainindex] > nodes[otherindex]




