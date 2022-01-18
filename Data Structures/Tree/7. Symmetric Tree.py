101. Symmetric Tree
Easy
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)

============================================================================================================================================================

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        
        return self.isMirror(root.left,root.right)
    
    def isMirror(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot:
            return True
        elif not leftRoot or not rightRoot:
            return False
        else:
            return leftRoot.val == rightRoot.val and self.isMirror(leftRoot.left, rightRoot.right) and self.isMirror(leftRoot.right, rightRoot.left)
