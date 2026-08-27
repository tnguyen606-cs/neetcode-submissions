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
            - Space: O(h) for recursion stack
        
        Approach 2: interative DFS 
            - Create a stack to store the node
            - Create a map to store each node's height and its biggest diameter
            - After each children are processed, we compute:
                - height = 1 + max(leftHeight, rightHeight)
                - diameter = max(leftHeight + rightHeight, leftDinameter, rightDiameter)
            - Time: O(n)
            - Space: O(n)

        """

        stack = [root]
        hmap = { None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in hmap:
                stack.append(node.left)
            elif node.right and node.right not in hmap:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = hmap[node.left]
                rightHeight, rightDiameter = hmap[node.right]
                height = 1 + max(leftHeight, rightHeight)
                diameter = max(leftHeight + rightHeight, leftDiameter, rightDiameter)
                hmap[node] = (height, diameter)

        return hmap[root][1]



