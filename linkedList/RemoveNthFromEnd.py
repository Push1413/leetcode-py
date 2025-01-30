from linkedList.impl.LinkedList import LinkedList
from linkedList.impl.Node import Node


def removeNthFromEnd(head, n):
    res = Node(0,head)
    dummy = res

    for _ in range(n):
        head = head.next

    while head:
        head = head.next
        dummy = dummy.next

    dummy.next = dummy.next.next

    return res.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ans = removeNthFromEnd(ll.head, 2)
    ll.display(ans)
