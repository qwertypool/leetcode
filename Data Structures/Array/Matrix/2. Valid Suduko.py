36. Valid Sudoku
Medium
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.

===========================================================================================================================
# Approach 1:
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            d = {}
            for j in range(9):
                d[board[i][j]] = d.get(board[i][j], 0) + 1
                
            for key,value in d.items():
                    if key.isnumeric():
                        if value > 1:
                            print(key," ",value)
                            return False
            
                        
        for i in range(9):
            d = {}
            for j in range(9):
                d[board[j][i]] = d.get(board[j][i], 0) + 1
                
            for key,value in d.items():
                    if key.isnumeric():
                        if value > 1:
                            print(key," ",value)
                            return False
            
        for i in range(9):
            ls = []
            row = 3*(i//3)
            column = 3*(i%3)
            for j in range(9):
                if board[row + j//3][column + j%3].isnumeric():
                    if board[row + j//3][column + j%3] in ls:
                        return False
                    else:
                        ls.append(board[row + j//3][column + j%3])
            
            
        return True
                        
