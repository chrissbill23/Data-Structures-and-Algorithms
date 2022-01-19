# QUEUE in O(1) for enqueue and O(1) for dequeue but


class Queue:
    
    def __init__(self, data=None):
        self.__data = data or []
        self.__front = 0
    def append(self, value):
        #Enqueue method
        if self.isEmpty():
            self.__data = []
            self.__front = 0
        self.__data.append(value)
    def pop(self):
        #Dequeue method
        if self.isEmpty():
            raise IndexError('Queue is empty')
        value = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front += 1
        return value
    def isEmpty(self):
        return self.__front == len(self.__data)
    def __len__(self):
        return len(self.__data) - self.__front
    def __str__(self):
        return ', '.join(self.__data[:self.__front-len(self.__data)-1:-1])
    def __repr__(self):
        return self.__str__()       
    
'''if __name__ == "__main__":
    q = Queue(["a", "b", "c"])
    print(q, len(q))
    
    q = Queue()
    print(q, len(q))
    
    q.append('a')
    print(q, len(q))
    q.append('b')
    print(q, len(q))
    q.append('c')
    print(q, len(q))
    q.pop()
    print(q, len(q))
    q.pop()
    print(q, len(q))
    q.pop()
    print(q, len(q))
    print(q.isEmpty())
    q.append('a')
    print(q, len(q))
  '''
