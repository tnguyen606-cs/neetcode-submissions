# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Given:
            BST root: 1<= k <= nodes <= 10k
            kth smallest value (1-indexed) in the tree
            Return the value at kth index in the tree

        Approach: Iteration Inorder DFS
            Since the tree is BST, left < node < right
            Stack store the value in increasing order starting from left to right
            Create a counter to count the number of stored value
            if counter == k: return the current node
            Time: O(n)
            Space: O(n)

        """

        if not root:
            return 0

        curr = root
        stack = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

