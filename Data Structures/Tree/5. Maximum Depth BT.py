104. Maximum Depth of Binary Tree
Easy
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

================================================================================================
================================================================================================

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        q.append(None)
        depth = 1
        while q:
            node = q.popleft()
            if node != None:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                if len(q) != 0:
                    q.append(None)
                    depth += 1
        return depth

================================================================================================
================================================================================================

            
