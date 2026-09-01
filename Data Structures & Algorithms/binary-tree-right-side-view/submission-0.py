# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Given:
            - BT root: 0 <= nodes <= 100
            - Return a LL of values that are visible from the right side in an ordered from top to bottom
            - For every level, we find the right most node
        
        Approach: Iterative BST
            - Create a queue starts from the root 
            - Create a response 
            - At next level, add the left and right child:
            - Remove the left most value from the queue
            - Append the last value left from queue to response list
            Time: O(n)
            Space: O(n)

        """

        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if i == qLen - 1:
                    res.append(node.val)
        
        return res