# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: Both nodes are None (we've reached the bottom successfully)
        if not p and not q:
            return True
        
        # Case 2: One is None and the other isn't (structural mismatch)
        if not p or not q:
            return False
        
        # Case 3: Both have values. They are identical ONLY if:
        # 1. Their current values are equal
        # 2. Their left subtrees are identical
        # 3. Their right subtrees are identical-
        return (p.val == q.val) and \
               self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
