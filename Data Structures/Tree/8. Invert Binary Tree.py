226. Invert Binary Tree
Easy
Given the root of a binary tree, invert the tree, and return its root.

# Recusrive approach:

def invertTree(self, root):
  if root:
    invert = self.invertTree
    root.left, root.right = invert(root.right), invert(root.left)
    return root

===============================================================================================================


#Iterative Approach:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
