from linkedListSupport import LinkedList
from linkedListSupport import Node

# Natural Solution

def partition(node, x):
    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None

    while(node != None):
        prox = node.next
        node.next = None

        if(node.value < x):
            if(beforeStart == None):
                beforeStart = node
                beforeEnd =  node
            else:
                beforeEnd.next = node
                beforeEnd = node
        else:
            if(afterStart == None):
                afterStart = node
                afterEnd = afterStart
            else:
                afterEnd.next = node
                afterEnd = node
        
        node = prox
    
    if(beforeStart == None):
        return afterStart
    
    beforeEnd.next = afterStart
    return beforeStart

# Tests

myLinkedList = LinkedList()

myLinkedList.add_to_head(2)
myLinkedList.add_to_tail(5)
myLinkedList.add_to_tail(4)
myLinkedList.add_to_tail(10)
myLinkedList.add_to_tail(3)
myLinkedList.add_to_tail(5)
myLinkedList.add_to_tail(8)
myLinkedList.add_to_tail(7)
myLinkedList.add_to_tail(4)
myLinkedList.add_to_tail(1)

myLinkedList.status()

myLinkedList.set_head(partition(myLinkedList.head, 4))

myLinkedList.status()