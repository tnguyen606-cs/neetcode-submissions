# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        """
        DFS - Inorder
        diff = L's longest height - R's longest height
        
        return diff > 1

        time: O(logn) - best; O(n) - worst
        space: O(logn) - best; O(n) - worst
        """

        if not root:
            return True

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root:  Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))










        