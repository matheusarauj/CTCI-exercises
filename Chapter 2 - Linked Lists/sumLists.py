from linkedListSupport import LinkedList
from linkedListSupport import Node

# Natural Solution

def sumLists(l1, l2, carry):
    if(l1 == None and l2 == None and carry == 0):
        return None
    
    result = Node()
    value = carry

    if(l1 != None):
        value += l1.value
    if(l2 != None):
        value += l2.value

    result.value = value%10

    if(l1 != None or l2 != None):
        more = sumLists(None if l1 == None else l1.next,
                        None if l2 == None else l2.next,
                        1 if value >= 10 else 0)
        result.set_next(more)

    return result

# Tests

myLinkedList1 = LinkedList()
myLinkedList2 = LinkedList()

myLinkedList1.add_to_head(7)
myLinkedList1.add_to_tail(1)
myLinkedList1.add_to_tail(6)

myLinkedList2.add_to_head(5)
myLinkedList2.add_to_tail(9)
myLinkedList2.add_to_tail(2)

myLinkedList1.status()
myLinkedList2.status()

myLinkedList1.set_head(sumLists(myLinkedList1.head, myLinkedList2.head, 0))

myLinkedList1.status()