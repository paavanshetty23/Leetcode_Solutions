class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Two children case → find inorder successor
                mini = self.fmini(root.right)
                root.val = mini.val
                root.right = self.deleteNode(root.right, mini.val)

        return root

    def fmini(self, node: Optional[TreeNode]):
        while node.left:
            node = node.left
        return node

