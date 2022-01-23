# HEAP module:Heap (Base abstract class); Minheap and Maxheap concrete classes
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
        self.__values[index] = self.__values[len(self.__values)-1] 
        val = self.__values.pop()
        self.heapifyDown(index)
        return val
    
    def  poll(self):
        return self.removeNode(len(self.__values)-1)
    
    def  peek(self):
        return self.removeNode(0)
    
    def __printHelper(self, currind):
        if currind >= len(self.__values) or currind < 0:
            return ''
        sL = ''
        sR = ''
        if self.hasLeftChild(currind):
            sL = self.__printHelper(self.leftChild(currind))
        if self.hasRightChild(currind):
            sR = self.__printHelper(self.rightChild(currind))
        return str(self.__values[currind])+'-->('+sL+','+sR+')'
    
    def __str__(self):
        return self.__printHelper(0) 
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.__values)
    
    def __getitem__(self, key):
        return self.__values[key]

class MinHeap(Heap):
    def compare(self, mainindex, otherindex):
        nodes = self.getNodes()
        return nodes[mainindex] < nodes[otherindex]
class MaxHeap(Heap):
    def compare(self, mainindex, otherindex):
        nodes = self.getNodes()
        return nodes[mainindex] > nodes[otherindex]
        
