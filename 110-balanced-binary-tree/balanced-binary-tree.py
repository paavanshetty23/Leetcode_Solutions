class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = height(node.left)
            if lh < 0:
                return -1
            rh = height(node.right)
            if rh < 0:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)

        return height(root) >= 0
