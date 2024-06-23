"""
Minimum Path Sum
Difficulty: Medium
https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

Solution 2D DP
---------------
As problem states the path from an element have two options when doing a DFS, either right or down.
Target is to reach the right corner, so we do a top-bottom approach.
Calculate the possible sum of top row and left most column. Because it is the base case in DP, 
in top row the grid[0][i] += grid[0][i-1], since left is only possible no top elements are there,
in first column the grid[i][0] += grid[i-1][0], since only top is available left is out of bounds.
We can start from element 1 ... n(no of col), 1 ... m(no of rows), for rest of elements.
The sum of a element will be minimum of it's up and left dp sum.

eg: 1   3   1
    1   5   1
    4   2   1
here we calculate the first row and col sum as base case
then;   1   4   5
        2   5   1
        6   2   1
Now from 1 ... n and 1 ... m, grid[1][1], ie, 5, we get min(grid[i-1][j], grid[i][j-1])
ie, top and left, her min is 2, so grid[1][1] = 5 + 2 = 7 now

    1   4   5
    2   7   1
    6   2   1
At last after all computation we get final answer in right corner;
    1   4   5
    2   7   6
    6   8   7
O/P: is 7
"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for colIndex in range(1, m):
            grid[0][colIndex] += grid[0][colIndex-1]
        
        for rowIndex in range(1, n):
            grid[rowIndex][0] += grid[rowIndex-1][0]
        
        for rowIndex in range(1, n):
            for colIndex in range(1, m):
                # sum add with min of top or left
                grid[rowIndex][colIndex] += min(grid[rowIndex-1][colIndex], grid[rowIndex][colIndex-1])
        # last row , col
        return grid[-1][-1]

# Testing
sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(sol.minPathSum([[1,2,3],[4,5,6]]))
