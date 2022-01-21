112. Path Sum
Easy

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
  
 ======================================================= =======================================================  
  
# Approach 1:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
        
        targetSum -= root.val 
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
            
             
