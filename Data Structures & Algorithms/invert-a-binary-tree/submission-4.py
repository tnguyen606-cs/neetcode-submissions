# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given: 
            BT's root
            1 <= node.length <= 100
        Return:
            Inverted root
        Approach: BFS
            everynode, swap its left and right children
            - start from the root
            - for each node, swap its children
            - then push the (new) left and right children into a queue
            - continue until every node has been processed
            Time:O(n)
            Space: O(n)

        Approach: DFS
            Use recursion to invert the tree in the top-down manner
            - At each node, swap the left and right children
            - Then recursively invert the left subtree
            - Recursively invert the right subtree
            Because every subtree is itself a smaller binary tree, recursion naturally handles
            Time: O(n)
            Space: O(n) for recursion stack

        Approach: Iterative DFS
            Iterative DFS inverts BT using an explicit stack
            - visit each node
            - swap its left and right subtree
            - continue the process for its children
            Process:
            - push the root into the stack
            - pop the top node, swap its children
            - push its children onto the stack if they exist
            - continue until the stack is empty
        Trade-offs between 2 DFSs: the iterative DFS works better if the recursion stack is too large

        """
        
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
