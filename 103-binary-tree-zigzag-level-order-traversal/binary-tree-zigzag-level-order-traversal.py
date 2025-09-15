# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        if not root:
            return res
        
        queue = deque()
        queue.append(root)

        ltr = True

        while queue:
            size = len(queue)

            row = [0] * size

            for i in range(size):
                node = queue.popleft()

                index =i if ltr else (size-1-i) 

                row[index]= node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ltr = not ltr

            res.append(row)

        return res
        