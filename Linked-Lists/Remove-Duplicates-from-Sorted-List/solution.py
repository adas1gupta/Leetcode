# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev_ptr = head
        crsr = head.next

        while crsr:
            if crsr.val == prev_ptr.val:
                prev_ptr.next = crsr.next
            else:
                prev_ptr = prev_ptr.next
    
            crsr = crsr.next
        
        return head
