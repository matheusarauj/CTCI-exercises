from linkedListSupport import LinkedList
from linkedListSupport import Node

# Natural Solution

def intersection(node1, node2):
    n1 = node1
    n2 = node2
    s1 = 0
    s2 = 0

    if(n1 == None or n2 == None):
        return None

    while(n1.next != None):
        n1 = n1.next
        s1 += 1
    
    while(n2.next != None):
        n2 = n2.next
        s2 += 1

    if n1 != n2:
        return None

    shorter = node1 if s1 < s2 else node2
    longer = node2 if s1 < s2 else node1

    longer = getKthNode(longer, abs(s1 - s2))

    while(shorter != longer):
        shorter = shorter.next
        longer = longer. next

    return longer

def getKthNode(longer, k):

    while(k <= 0):
        longer = longer.next
        k -= 1

    return longer



    

    

