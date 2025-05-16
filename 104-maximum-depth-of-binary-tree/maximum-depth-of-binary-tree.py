class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.iter(root, 0, 0)

    def iter(self, node: Optional[TreeNode], count: int, maxi: int) -> int:
        if node is None:
            return maxi
        count += 1
        left_max = self.iter(node.left, count, maxi)
        right_max = self.iter(node.right, count, maxi)
        return max(count, left_max, right_max)
