class Stack():
    def __init__(self,arr:list=[]):
        self.items=arr
    
    def push(self,item):
        self.items.append(item)
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items)==0
    
    def pop(self):
        if(not self.isEmpty):
            return self.items.pop()
        return None
        
    def size(self):
        return len(self.items)
    
class Queue:
    def __init__(self,arr:list):
        self.items=arr

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if(not self.isEmpty):
            return self.items.pop(0)
        return None

    def isEmpty(self):
        return len(self.items)==0
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

class LinkedList:
    def __init__(self):
        pass