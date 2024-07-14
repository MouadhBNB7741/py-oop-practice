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

class DoubleLinkedList:
    class Node:
        def __init__(self,val):
            self.value=val
            self.next=None
            self.prev=None

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
        newNode.prev=last

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
            current.prev= None
            current = None
            return

        while current and current.value != data:
            previous = current
            current = current.next

        if not current:
            print("Data not found in the list.")
            return

        previous.next = current.next
        current.prev = previous
        current = None

    def getHead(self):
        return self.head

c=DoubleLinkedList()

c.append(5)
c.append(6)
c.append(7)
c.append(8)
d=c.getHead()
c.printList()
print (d.prev)
print(d.value)
print(d.next.value)
d=d.next
print (d.prev.value)
print(d.value)
print(d.next.value)
d=d.next
print (d.prev.value)
print(d.value)
print(d.next.value)
d=d.next
print (d.prev.value)
print(d.value)

