from linkedList.impl.LinkedList import LinkedList

def reverseList(head):
    curr = head
    prev = None
    while(curr!=None):
        forw = curr.next
        curr.next = prev
        prev = curr
        curr = forw
    return prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("Original Linked List:")
    ll.display()

    reversed_head = reverseList(ll.head)
    
    print("\nReversed Linked List:")
    ll.display(reversed_head)
