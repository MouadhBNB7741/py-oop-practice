class Stack():
    def __init__(self,arr:list):
        self.items=arr
    
    def push(self,item):
        self.items.append(item)
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def isEmpty(self):
        return len(self.items)==0
    
    def pop(self):
        self.items.pop()
    
    def size(self):
        return len(self.items)
    
