from linkedList.impl.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node at the end of the linked list
    def append(self, val):
        new_Node = Node(val)
        if self.head==None:
            self.head = new_Node
        else:
            curr = self.head
            while curr.next!= None:
                curr = curr.next
            curr.next = new_Node

    # Display the linked list
    def display(self, head=None):
        current = current = head if head else self.head
        elements = []
        while current:
            elements.append(current.val)
            current = current.next
        print(" -> ".join(map(str, elements)))



    # Insert a node at a specific position
    def insert(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Delete a node by value
    def delete(self, val):
        if not self.head:
            print("List is empty")
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.val != val:
            current = current.next
        if current.next:  # If the target node is found
            current.next = current.next.next
        else:
            print(f"Value {val} not found in the list")


