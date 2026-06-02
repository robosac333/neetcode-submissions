# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        dummy = ListNode(head.val)
        curr = head.next
        while curr:
            prev = curr
            curr = curr.next
            prev.next = dummy
            dummy = prev
            #print(dummy.val)
        return dummy
        
