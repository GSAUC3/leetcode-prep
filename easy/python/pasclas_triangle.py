# Question:  118 (https://leetcode.com/problems/pascals-triangle/)
#  Pascal's Triangle 
# Easy
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
#


# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:

# Input: numRows = 1
# Output: [[1]]

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = [[1],[1,1]]
        if numRows ==1:
            return [[1]]
        elif numRows ==2:
            return r
        else: 
            for i in range(2,numRows):
                r.append(
                    [1] +[ 
                    r[i-1][j]+r[i-1][j+1] for j in range(len(r[i-1])-1) 
                    ]  +[1]
                    )
            
            return r