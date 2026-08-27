# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given:
            BT's root: 1<= root <= 100
            diameter: length of the longest path between any two nodes
            path's length: number of edges between the nodes
        Result:
            return the diameter

        Approach 1: recursive DFS
            Idea: diameter = sum of max(left) and max(right)
            - Recursively find the longest path of the left
            - Recursively find the longest path of the right
            - Return sum
            - Time: O(n)
            - Space: O(n) for recursion stack
        
        Approach 2: interative DFS 
            - Create a stack to store the node
            - Create a map to store each node's height and its biggest diameter
            - After each children are processed, we compute:
                - height = 1 + max(leftHeight, rightHeight)
                - diameter = max(leftHeight + rightHeight, leftDinameter, rightDiameter)
            - Time: O(n)
            - Space: O(n)

        """

        maxLength = 0

        def dfs(root): 
            nonlocal maxLength
            
            if not root:
                return 0

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            maxLength = max(maxLength, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return maxLength