from linkedListSupport import LinkedList
from linkedListSupport import Node

# Natural Solution

def kthToLast(head, pos):
    node = head
    if node = None:
        return 0
    cont = 1
    while(node.next != None):
        cont += 1
        node = node.next

    kth = cont - pos
    node  = head
    while(kth > 0):
        node = node.next
        kth -= 1

    return node.value

# Tests

myLinkedList = LinkedList()

myLinkedList.add_to_head(2)
myLinkedList.add_to_tail(5)
myLinkedList.add_to_tail(4)
myLinkedList.add_to_tail(10)
myLinkedList.add_to_tail(3)
myLinkedList.add_to_tail(5)
myLinkedList.add_to_tail(7)
myLinkedList.add_to_tail(4)
myLinkedList.add_to_tail(1)

myLinkedList.status()

print(kthToLast(myLinkedList.head, 5))
print(kthToLast(myLinkedList.head, 1))
print(kthToLast(myLinkedList.head, 8))