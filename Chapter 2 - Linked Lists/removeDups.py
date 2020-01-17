from linkedListSupport import LinkedList
from linkedListSupport import Node

# Natural Solution
def removeDups1(node):
    setAux = set()
    prev = None
    while(node != None):
        if(setAux.__contains__(node.value)):
            prev.next = node.next
        else:
            setAux.add(node.value)
            prev = node
        node = node.next

# No buffer allowed Solution
def removeDups2(node):
    current = node
    while(current != None):
        runner = current
        while(runner.next != None):
            if(runner.next.value == current.value):
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

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

removeDups1(myLinkedList.head)

myLinkedList.status()

myLinkedList.add_to_tail(10)
myLinkedList.add_to_tail(3)

myLinkedList.status()

removeDups2(myLinkedList.head)

myLinkedList.status()

