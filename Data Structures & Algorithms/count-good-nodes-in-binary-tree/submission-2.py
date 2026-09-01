# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Given:
            - BT root: 1 <= nodes <= 100
            - Good node means no ascendant node values > its value
            - Return number of good nodes
            - The root is a good node because no node above it that is > itself

        Approach: Iterative BFS
            - Create a queue to store a pair of [node, max ascendant node values]
            - Create a res to store the number of good nodes
            - While queue is not empty:
                - while at the current level:
                    - pop the left most value in the queue
                    - update the max ascendant node values

                    if current node val > max node values:
                        increment the res by 1

                    if left node exist:
                        append left node to the queue 
                    if right node exist:
                        append right node to the queue

            Time: O(n)
            Space: O(n)
        """
        goodNodes = 0
        q = deque([(root, -float('inf'))])
        
        while q:
            node, maxNode = q.popleft()

            if maxNode <= node.val:
                goodNodes += 1

            maxNode = max(maxNode, node.val)

            if node.left:
                q.append((node.left, maxNode))
            if node.right:
                q.append((node.right, maxNode))

        return goodNodes

