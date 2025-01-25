from linkedList.impl.LinkedList import LinkedList
def hasCycle(head):
    visited= set()
    curr = head
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False


# update ll impl so that cycle can be created 
if __name__ =='__main__':
    ll = LinkedList()
    ll.append(3)
    ll.append(2)
    ll.append(0)
    ll.append(-4)
    print(hasCycle(ll.head))

