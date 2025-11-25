# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        ptr = head
        def dfs(left, right):
            nonlocal ptr
            if left > right: return None

            mid = left + (right - left) // 2

            left_tree = dfs(left, mid - 1)

            node = TreeNode(ptr.val)
            ptr = ptr.next
            node.left = left_tree
            node.right = dfs(mid + 1, right)

            return node
        
        return dfs(0, length - 1)
            