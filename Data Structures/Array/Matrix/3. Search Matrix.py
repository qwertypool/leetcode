Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


Approach 1:
1. Flatten the matrix into a single array
2. Use Binary search to find the target

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_len = len(matrix)
        column_len = len(matrix[0])
        ls = [matrix[i][j] for i in range(row_len) for j in range(column_len)]
        left = 0
        right = len(ls)-1
        while left <= right:
            mid = left + (right - left)//2
            if target == ls[mid]:
                return True
            elif target > ls[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
      
      
      
Approach 2:
1. Use the advantage of the properties of matrix given, to find out the row in which our target could possibly be.
2. Once you get the targeted row, implement binary search in that row.

        position = 0
        ls = [] 
        for i in range(row_len):
            if target > matrix[i][column_len-1]:
                continue
            else:
                position = i
                break
                
        ls[:] = matrix[position]  
        left = 0
        right = len(ls)-1
        while left <= right:
            mid = left + (right - left)//2
            if target == ls[mid]:
                return True
            elif target > ls[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
      
      
      
Approach 3:
1. Straight forward brute force approach (surprisingly very fast :P)

		for i in matrix:
            if target in i:
                return True
        return False
      
      
      
Approach 4:
1. Start with the first row and last column of the matrix
2. If the number is less than the target then increase the row index(because greater numbers can be found below, as per the question)
3. If the number is greater than the target then decrease the column index(as the matrix is sorted in ascending order in the columns also)

        rows, cols =  len(matrix), len(matrix[0]) 
        r, c = 0, cols-1
        
        while 0 <= r < rows and 0 <= c < cols:
            
            num = matrix[r][c]
            if num == target:
                return True
            elif num < target:
                r += 1
            else:
                c -= 1
        
        return False
