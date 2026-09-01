# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given:
            - BT root
            - Return level order traversal as a nested list
            - each sublist contains values at a particular level in the tree

        Approach: Iterative BFS with queue 
            - Queue store the first node - root
            - While queue:
                pop the first element
                while in current queue length:
                    append all children of the left nodes
                    append all children of the right nodes
                add the level to the response
            time: O(h * m), h is height, m is number of leaf nodes
            space: O(n)

        """

        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            subList = []
            for i in range(len(queue)):
                node = queue.popleft()
                subList.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if subList:
                res.append(subList)
        
        return res




