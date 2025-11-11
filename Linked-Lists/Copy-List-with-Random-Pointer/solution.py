"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = Node(0)
        
        curr = head
        nodes = {}

        while curr:
            node = Node(curr.val)
            nodes[curr] = node
            curr = curr.next
        
        curr = head
        dummy.next = nodes[head]
        crsr = dummy.next
        while curr:
            crsr.next = nodes[curr.next] if curr.next else None
            crsr.random = nodes[curr.random] if curr.random else None
            crsr = crsr.next
            curr = curr.next
        
        return dummy.next