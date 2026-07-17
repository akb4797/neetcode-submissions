# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, a, b):
        
        if not a and not b:
            return True
        
        if not a or not b:
            return False 

        if(a.val == b.val) and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right):
            return True
            

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        '''
        - get subtree root
        - iterate main tree
        - if subtree root detected, do tree comparison
        -  
        '''

        if not root:
            return False

        
        if self.isSameTree(root, subRoot):
            return self.isSameTree(root, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

            