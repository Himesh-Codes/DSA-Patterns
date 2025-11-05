"""
Longest Increasing Path in a Matrix

Difficulty: Hard

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1

Solution (Brute Force)
----------
Do DFS from all the cells and keep track of the maximum length path found.
Time complexity = O(4 ^ M * N) as each cell traverse 4 directions; Space = O(M * N) due to recursion stack.

Steps
-------
For every cell (i, j), do DFS:
- Explore all 4 directions.
- Move only if the next cell's value > current cell's value.
- While backtrack take the max path length among all possibilities.

Solution (Optimised) : DFS + DP Memoization
----------
Using DP memoization we can avoid recomputation of longest increasing path value from each cell.
We will avoid computation if DP[i][j] ie, a cell value exists.
Time = O(N*M) Space = O(N * M)

Intuition
----------
We can reduce the complexity on recomputation of longest increasing path from each cell by Memoization.
DP[i][j] is filled by taking maximum value of path returned from DFS(neighbours).

Steps
-------
Do a DFS from every cell to find the longest increasing path starting at that cell, 
cache the result so each cell is computed once.

We define:
- dp[i][j] = length of longest increasing path starting at cell (i, j)
- If dp[i][j] is already computed (nonzero), return it immediately. Otherwise compute as:
- dp[i][j] = 1 + max( dfs(neighbor) for neighbors with value > matrix[i][j] )

"""

from typing import List


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    maxLen = 0

    def dfs(i,j):
        if dp[i][j]:
            return dp[i][j]
        
        best = 1
        for dirX, dirY in directions:
            x, y = i + dirX, j + dirY

            if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                best = max(best, 1 + dfs(x,y))
        dp[i][j] = best
        return best
    
    for indexI in range(m):
        for indexJ in range(n):
            maxLen = max(maxLen, dfs(indexI, indexJ))
    return maxLen


print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))