# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        if root is None:
            return False

        subsum =targetSum-root.val

        if subsum==0 and root.left is None and root.right is None:
            return True

        left = self.hasPathSum(root.left,subsum) if root.left else False
        right = self.hasPathSum(root.right,subsum) if root.right else False

        return left or right
        