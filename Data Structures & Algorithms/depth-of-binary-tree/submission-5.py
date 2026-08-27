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
            Idea: depth = 1 + max(left, right)
            - if root is none: return 0
            - Recursively compute the depth of the left subtree
            - Recursively compute the depth of the right subtree.
            - return max(left, right) + 1
            - Time: O(n)
            - Space: O(n) for recursion stack

        Approach 1: Iterative DFS
            Idea: depth = 1 + max(lef, right)
            - if root is none: return 0
            - stack store a pair of the current node and its depth in the tree
            - while stack is not empty:
                - pop a node
                - we update the max depth of the current node
                - we push its left and right onto the stack if they exists
            - Time: O(n)
            - Space: O(n)
        """

        if not root:
            return 0

        stack = [[root, 1]]
        maxDepth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                maxDepth = max(maxDepth, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return maxDepth

