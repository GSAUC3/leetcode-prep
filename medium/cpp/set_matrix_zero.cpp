//  Question: 1170 (https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/)
//  73. Set Matrix Zeroes
//  Medium

//  Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

//  You must do it in place.

#include <iostream>
#include <vector>
#include <utility> // for std::pair

using namespace std;

class Solution
{
public:
    int height;
    int width;

    void setZeroes(vector<vector<int>> &matrix)
    {

        vector<std::pair<int, int>> pos;

        this->height = matrix.size();
        this->width = matrix[0].size();

        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                if (matrix[i][j] == 0)
                {
                    pos.emplace_back(i, j);
                }
            }
        }

        std::vector<std::pair<int, int>>::iterator it;
        for (it = pos.begin(); it != pos.end(); ++it)
        {
            change_col_row(matrix, *it);
        }
    }

    void change_col_row(vector<vector<int>> &v, std::pair<int, int> &p)
    {
        int x = p.first;
        int y = p.second;
        for (int i = 0; i < this->height; i++)
        {
            v[i][y] = 0;
        }
        for (int j = 0; j < this->width; j++)
        {
            v[x][j] = 0;
        }
    }
};