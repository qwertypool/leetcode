# Reshape Matrix:

#Approach 1: Straight Forward Approach
---------------------------------------
class Solution(object):
    def matrixReshape(self, mat, r, c):

        rows = len(mat)
        columns = len(mat[0])
        
        if rows*columns != r*c:
            return mat
        
        columnCount = c
        resColumn = []
        result = []
        
        for i in range(rows):
            for j in range(columns):
                columnCount -= 1
                resColumn.append(mat[i][j])
                if columnCount == 0:
                    columnCount = c
                    result.append(resColumn)
                    resColumn = []
        return result
        
 ===========================================================================================
 
 # Approach 2: 
 1. First check if the number of rows & columns in the original given matrix is equal to or not the given r & c
 2. If true, then flatten the matrix into 1D Array
 3. Re-construct the Matrix
 
 class Solution:
    def matrixReshape(self, nums, r, c):
    
        if len(nums) * len(nums[0]) != r * c: return nums # check
        
        l = [n for num in nums for n in num] # flatten 2-d array -> 1-d array 
        
        return [l[i: i+c] for i in range(0, len(l), c)] # reshape vector -> matrix
 
