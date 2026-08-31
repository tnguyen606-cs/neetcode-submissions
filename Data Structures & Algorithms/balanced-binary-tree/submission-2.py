# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Intuition:
            Balanced tree is an even tree across branches
            Height-balanced BT is its left and its right subtrees differ <= height of 1
            If tree is empty, return true
            If tree is balanced in height, return true
            Otherwise, return false

        Approach:
            1. Recursive DFS
            - Idea: check if current subtree is balanced and its height
            - If any node, the height difference > 1, mark it unbalanced

        """

        def dfs(root):
            if not root:
                return [True, 0]

            leftH, rightH = dfs(root.left), dfs(root.right)
            isBalanced = leftH[0] and rightH[0] and abs(leftH[1] - rightH[1]) < 2

            return [isBalanced, 1 + max(leftH[1], rightH[1])]

        return dfs(root)[0]