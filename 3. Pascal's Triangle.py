Question:
118. Pascal's Triangle
Easy
Given an integer numRows, return the first numRows of Pascal's triangle.


# Approach 1:
class Solution(object):
    def generate(self, numRows):
        pascalRow = []
        for i in range(numRows):
            row = []
            if i == 0:
                row.append(1)
            else:
                for j in range(i+1):
                    if j==0 or j==i:
                        row.append(1)
                    else:
                        first = pascalRow[i-1][j-1]
                        second = pascalRow[i-1][j]
                        row.append(first+second)
        
            pascalRow.append(row)
        return pascalRow
        
======================================================================================

# Approach 2:
# 1. Generate a triangle consisting of all 1's
# 2. Iterate through the loops and successively keep adding the result for every element of the array
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]*i for i in range(1,numRows+1)]
        for i in range(2, numRows):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result
      
