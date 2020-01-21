from linkedListSupport import LinkedList
from linkedListSupport import Node

# Natural Solution

def deleteMiddleNode(head, value):
    node = head

    while(node.next.next != None):
        if node.next.value == value:
            node.next = node.next.next
            break
        node = node.next

    
# Tests

myLinkedList = LinkedList()

myLinkedList.add_to_head(4)
myLinkedList.add_to_tail(5)
myLinkedList.add_to_tail(4)
myLinkedList.add_to_tail(10)

myLinkedList.status()
deleteMiddleNode(myLinkedList.head, 10)
myLinkedList.status()
