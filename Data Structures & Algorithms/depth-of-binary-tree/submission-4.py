# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given: root of a BT
            depth: number of nodes of the longest path from root

        Return: depth

        Approach 1: Recursion DFS
            start from the root
            - if root is none: return 0
            - find the longest path on the left subtree
            - find the longst path on the right subtree
            - return max(left, right)
            - Time: O(n)
            - Space: O(n) for recursion stack

        
        """

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1