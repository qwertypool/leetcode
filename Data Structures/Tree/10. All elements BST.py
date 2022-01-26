
1305. All Elements in Two Binary Search Trees
Medium
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

=========================================================================================
# Approach 1:
# Do inorder and using two pointers sort the tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        ls1, ls2 = [], []
        ls1 = self.traversal(root1,ls1)
        ls2 = self.traversal(root2,ls2)
        p1, p2 = 0, 0
        ls = [] 
        while p1 < len(ls1) and p2 < len(ls2):
            if ls1[p1]>ls2[p2]:
                ls.append(ls2[p2])
                p2 += 1
            elif ls1[p1]<ls2[p2]:
                ls.append(ls1[p1])
                p1 += 1
            else:
                ls.append(ls1[p1])
                ls.append(ls2[p2])
                p1 += 1
                p2 += 1
                
        if ls1[p1:]:
            ls.extend(ls1[p1:])
        if ls2[p2:]:
            ls.extend(ls2[p2:])
        return ls  
        
    def traversal(self,root,ls):
        if root:
            self.traversal(root.left,ls)
            ls.append(root.val)
            self.traversal(root.right,ls)
        return ls
            
