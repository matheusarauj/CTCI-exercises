from linkedListSupport import LinkedList
from linkedListSupport import Node

# Natural Solution

def palindrome(linkedList):
    aux = linkedList.copy()
    aux.reverse()

    node1 = linkedList.head
    node2 = aux.head

    while(node1 != None):
        if(node1.value != node2.value):
            return False
        node1 = node1.next
        node2 = node2.next
    
    return True

# Tests

myLinkedList = LinkedList()

myLinkedList.add_to_head(1)
myLinkedList.add_to_tail(4)
myLinkedList.add_to_tail(3)
myLinkedList.add_to_tail(4)
myLinkedList.add_to_tail(1)

print(palindrome(myLinkedList))
