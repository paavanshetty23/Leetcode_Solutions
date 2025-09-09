import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        # We use a deque for efficient appends and poplefts (O(1) time).
        # Each item in the queue is a tuple: (node, its position index).
        queue = collections.deque([(root, 0)])
        max_width = 0

        while queue:
            # The number of nodes at the current level.
            level_size = len(queue)
            
            # The first and last nodes of the current level.
            first_index = queue[0][1]
            last_index = queue[-1][1]

            # The width of the current level.
            current_width = last_index - first_index + 1
            max_width = max(max_width, current_width)

            # Process all nodes on the current level.
            for _ in range(level_size):
                node, index = queue.popleft()
                
                # Normalize indices to prevent integer overflow for deep trees.
                # A left child's index is 2*i, right child's is 2*i+1.
                # We normalize relative to the first node's index on the level.
                normalized_index = index - first_index
                
                if node.left:
                    queue.append((node.left, 2 * normalized_index))
                
                if node.right:
                    queue.append((node.right, 2 * normalized_index + 1))
        
        return max_width