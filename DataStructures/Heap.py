# HEAP module:Heap (Base abstract class); Minheap and Maxheap concrete classes
class Heap :
    def __init__(self):
        self.size = 0
        self.__values = []
        self.heapifyDown(0)
    def getNodes(self):
        return self.__values
    def hasParent(self, index):
        return 0 <= (index - 1) // 2  < self.size
    def parent(self, index):
        return (index - 1) // 2
    def hasLeftChild(self, index):
        return 0 <= 2*index + 1 < self.size
    def hasRightChild(self, index):
        return 0 <= 2*index + 2 < self.size
    def rightChild(self, index):
        r = 2*index + 2
        if r >= self.size:
            raise ValueError('The node given has not a right child')
        return r
    def leftChild(self, index):
        l = 2*index + 1
        if l >= self.size:
            raise ValueError('The node given has not a left child')
        return l
    def compare(self, mainindex, otherindex):
        raise NotImplementedError()
        
    def heapifyUp(self, index):
        while self.hasParent(index) and self.compare(index, self.parent(index)):
            newind = self.parent(index)
            tmp = self.__values[index]
            self.__values[index] = self.__values[newind]
            self.__values[newind] = tmp
            index = newind
    def heapifyDown(self, index):
        while self.hasLeftChild(index) and not(self.compare(index, self.leftChild(index))):
            newind = self.leftChild(index)
            tmp = self.__values[index]
            if self.hasRightChild(index) and self.compare(self.rightChild(index), newind):
                newind = self.rightChild(index)
            self.__values[index] = self.__values[newind]
            self.__values[newind] = tmp
            index = newind
        
    def addNode(self, value):
        self.size += 1
        self.__values.append(value)
        self.heapifyUp(self.size-1)
    def removeNode(self, index):
        if self.size == 0:
            raise ValueError('The tree is empty')
        if index >= self.size:
            raise ValueError('The node given is not in the tree')
        self.__values[index] = self.__values[self.size-1] 
        val = self.__values.pop()
        self.size -= 1
        self.heapifyDown(index)
        return val
    def  poll(self):
        return self.removeNode(self.size-1)
    def  peek(self):
        return self.removeNode(0)
    def __printHelper(self, currind):
        if currind >= self.size or currind < 0:
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

class MinHeap(Heap):
    def compare(self, mainindex, otherindex):
        nodes = self.getNodes()
        return nodes[mainindex] < nodes[otherindex]
class MaxHeap(Heap):
    def compare(self, mainindex, otherindex):
        nodes = self.getNodes()
        return nodes[mainindex] > nodes[otherindex]
    
            
'''if __name__ == "__main__":
    
    obj = MinHeap()
    obj.addNode(10); obj.addNode(15); obj.addNode(20); obj.addNode(17); obj.addNode(25); obj.addNode(5)
    #obj.peek()
    #obj.removeNode(1)
    print (obj)
    print (obj.getNodes())
    
    obj = MaxHeap()
    obj.addNode(10); obj.addNode(15); obj.addNode(20); obj.addNode(17); obj.addNode(25); obj.addNode(5)
    #obj.peek()
    #obj.removeNode(1)
    print (obj)
    print (obj.getNodes())
 '''
            
    
