# Question: 1170 (https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/)
# 73. Set Matrix Zeroes
# Medium

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.




from typing import List, Tuple

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.height = len(matrix)
        self.width = len(matrix[0])
        pos = []
        for i in range(self.height):
            for j in range(self.width):
                if matrix[i][j] == 0:
                    pos.append((i,j))
        
        for p in pos:
            self.change_col_row(matrix, p)
    
    def change_col_row(self, mat:List[List[int]] ,pos_:Tuple[int,int]):
        x,y = pos_
        # keep x constant and vary y
        for i in range(self.height):
            mat[i][y] = 0
        for j in range(self.width):
            mat[x][j] = 0 
    