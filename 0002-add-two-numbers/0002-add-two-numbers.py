# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)  # Dummy node to start the linked list
        current = dummyHead
        carry = 0

        while l1 or l2 or carry:
            x1 = l1.val if l1 else 0
            y1 = l2.val if l2 else 0
            add = x1 + y1 + carry
            carry = add // 10
            current.next = ListNode(add % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummyHead.next            


        
        


            
            

        

        