# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = list1, list2
        prev = ListNode()
        dummy = prev

        while first and second:
            if first.val < second.val:
                prev.next = first
                first = first.next
            else:
                prev.next = second
                second = second.next

            prev = prev.next
        
        if first:
            prev.next = first
        if second:
            prev.next = second

        return dummy.next