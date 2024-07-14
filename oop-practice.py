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
    class Node:
        def __init__(self,val):
            self.value=val
            self.next=None

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = self.Node(data)
        if not self.head:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def printList(self):
        current=self.head
        while(current):
            print(current.value)
            current=current.next

    def remove(self, data):
        current = self.head
        previous = None

        if not current:
            print("List is empty, nothing to remove.")
            return

        if current and current.value == data:
            self.head = current.next
            current = None
            return

        while current and current.value != data:
            previous = current
            current = current.next

        if not current:
            print("Data not found in the list.")
            return

        previous.next = current.next
        current = None
