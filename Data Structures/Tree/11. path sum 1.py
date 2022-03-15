112. Path Sum
Easy
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.


DFS Recursively
def hasPathSum1(self, root, sum):
    res = []
    self.dfs(root, sum, res)
    return any(res)
    
def dfs(self, root, target, res):
    if root:
        if not root.left and not root.right and root.val == target:
            res.append(True)
        if root.left:
            self.dfs(root.left, target-root.val, res)
        if root.right:
            self.dfs(root.right, target-root.val, res)

# DFS with stack
def hasPathSum2(self, root, sum):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right and val == sum:
            return True
        if curr.right:
            stack.append((curr.right, val+curr.right.val))
        if curr.left:
            stack.append((curr.left, val+curr.left.val))
    return False
    
# BFS with queue
def hasPathSum(self, root, sum):
    if not root:
        return False
    queue = [(root, sum-root.val)]
    while queue:
        curr, val = queue.pop(0)
        if not curr.left and not curr.right and val == 0:
            return True
        if curr.left:
            queue.append((curr.left, val-curr.left.val))
        if curr.right:
            queue.append((curr.right, val-curr.right.val))
    return False
	
def hasPathSum1(self, root, sum):
    if not root:
        return False
    if not root.left and not root.right and root.val == sum:
        return True
    return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
