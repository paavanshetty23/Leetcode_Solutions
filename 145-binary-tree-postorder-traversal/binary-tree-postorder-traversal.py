# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append((curr, False))  # Store node and a flag
                curr = curr.left
            else:
                curr, visited = stack.pop()
                if visited:
                    res.append(curr.val)
                    curr = None  # Important: Reset curr to prevent revisiting
                else:
                    stack.append((curr, True))  # Mark as visited
                    curr = curr.right
        return res

