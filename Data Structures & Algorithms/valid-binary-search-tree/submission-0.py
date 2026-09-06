# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Given:
            BT root: 1<= nodes <= 10k
            BST:
                - left subtree's nodes < node
                - right subtree's nodes > node
                - both left and right is valid BST
            Return true if a valid BST

        Approach 1: Iteration BST 
            Every node is within a valid range defined by its ancestors
            Use queue to check this level by level
                - start with the root, its ranges is -infinite,infinite
                - when we move to the left, its max value is the current node's value
                - when we move to the right, its min value is the current node's value
                - if any node violates its allowed range, return False

            Time: O(n)
            Space: O(n)

        """
        queue = deque([(root, float("-inf"), float("inf"))])
        while queue:
            node, minVal, maxVal = queue.popleft()

            if not (minVal < node.val < maxVal):
                return False
            if node.left:
                queue.append((node.left, minVal, node.val))
            if node.right:
                queue.append((node.right, node.val, maxVal))

        return True
