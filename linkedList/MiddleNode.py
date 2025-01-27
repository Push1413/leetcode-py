from linkedList.impl.LinkedList import LinkedList

def middleNode(head):
    oneStep = head
    twoStep = head
    while twoStep is not None and twoStep.next is not None:
        oneStep = oneStep.next
        twoStep = twoStep.next.next
    return oneStep

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    newHead = middleNode(ll.head)
    ll.display(newHead)



