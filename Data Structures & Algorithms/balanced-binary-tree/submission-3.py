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
            - Time, Space: O(n)
            2. Iterative DFS
            - Idea: Visit each node after its children
                    Once both children of a node are processed, we have their heights
                    Check:
                        - if height <= 1
                        - Save node's height = 1 + max(leftH, rightH)
                    If any node is unbalanced, return false immediately
        """

        if not root:
            return True

        stack = []
        heights = {} # store the height of each visited node
        node = root
        last = None

        while stack or node:
            # traverse all left nodes first
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]

                # If stored both subtrees
                if not node.right or last == node.right:
                    stack.pop()
                    left = heights.get(node.left, 0)
                    right = heights.get(node.right, 0)

                    if abs(left - right) > 1:
                        return False

                    heights[node] = 1 + max(left, right)
                    last = node
                    node = None
                # Traverse the right subtrees
                else:
                    node = node.right

        return True
