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
        return str(self.__data[:self.__front-len(self.__data)-1:-1])
        
    def __repr__(self):
        return self.__str__() 
    
class PriorityElement:
    def __init__(self, keydata:tuple):
        self.key = keydata[0]
        self.data = keydata[1]
    def __hash__(self):
        return hash((self.key,self.data))
    def __eq__(self, other):
        if not isinstance(other, type(self)): 
            return False
        return self.key == other.key and self.data == other.data
    def __le__(self, other):
        return self.data <= other.data
    def __ge__(self, other):
        return self.data >= other.data
    def  __lt__(self,other):
        return self.data < other.data
    def  __gt__(self,other):
        return self.data > other.data
        
    def __str__(self):
        return ' ||Key: '+ str(self.key)+';Data: '+str(self.data)+'|| '
        
class PriorityQueue(Queue):
    
    def __init__(self):
        super().__init__()
        
    def append(self, value: PriorityElement):
        raise NotImplementedError()
        
    def top(self)->PriorityElement:
        raise NotImplementedError()
        
    def pop(self)->PriorityElement:
        raise NotImplementedError()
        
    def isEmpty(self):
        return self.__len__() == 0

