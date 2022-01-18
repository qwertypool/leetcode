
144. Binary Tree Preorder Traversal
Easy
Given the root of a binary tree, return the preorder traversal of its nodes' values.
====================================================================================================================
# Recursive approach
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ls = []
        self.preorder(root,ls)
        return ls
        
    def preorder(self,root,ls):
        if root:
            ls.append(root.val)
            self.preorder(root.left, ls)
            self.preorder(root.right, ls)
            
====================================================================================================================
# iteratively
def preorderTraversal(self, root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res
