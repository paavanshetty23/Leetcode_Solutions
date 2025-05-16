# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        result: List[List[int]] = []
        queue = deque([root])
        
        # Standard BFS with a queue, tracking levels by queue length
        while queue:
            level_size = len(queue)
            level_vals: List[int] = []
            
            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                
                # Enqueue children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add this level's values to the result
            result.append(level_vals)
        
        return result