# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        sortedHead = None
        
        if list1.val < list2.val:
            sortedHead = list1
            list1 = list1.next
        else:
            sortedHead = list2
            list2 = list2.next
        
        traverseHead = sortedHead

        
        while list1 and list2:
            if list1.val < list2.val:
                traverseHead.next = list1
                list1 = list1.next
            else:
                traverseHead.next = list2
                list2 = list2.next
            traverseHead = traverseHead.next
        
        traverseHead.next = list1 if list1 else list2
    
        return sortedHead
        

        




        

        

        