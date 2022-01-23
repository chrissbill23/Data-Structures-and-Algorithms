from DataStructures import MinHeap, MaxHeap

class KthLargest:

    def __init__(self, k: int, data):
        #O(nlog(n) + k)
        data = sorted(data, reverse=True)
        self.__data = MinHeap(data[:k][::-1])
        self.k = k
        
    def add(self, val):
        #O(log(n))
        self.__data.addNode(val)
        if len(self.__data) > self.k:
            self.__data.peek()
        return self.__data[0]
        
    def getKLargest(self):
        return self.__data[0]
        
        