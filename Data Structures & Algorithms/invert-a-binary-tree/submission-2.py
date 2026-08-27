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

        """
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.right, node.left = node.left, node.right
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
