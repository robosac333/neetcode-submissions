# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        length = len(nodes)-n

        if length == 0:
            return head.next   
        
        i =0
        prev, cut, attach = None, head, head.next
        dummy = cut
        while i<length:
            prev = cut
            if attach:
                attach = attach.next
            cut = cut.next
            i+=1

        if prev:
            prev.next = attach
        return dummy

            
