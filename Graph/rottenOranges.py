"""
Rotting Oranges
Difficulty: Medium

https://leetcode.com/problems/rotting-oranges/description/

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten,
 because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Solution
---------
1) Do  a BFS search inside the array.
2) Inorder to do that we need to find and iterate the BFS on rotten oranges (ie, value with 2).
We should traverse the 2D array first to get count of the fresh oranges, and add the rotten oranges into queue. O(N2)
3) Then do the BFS on the oranges, until the queue is getting empty, O(N2), in 4 directions i+1, j+1, i-1, j-1.
Change if and only if it is the fresh orange (value 1) into rotten (value 2), and add into queue.
4) After one iteration is completed in BFS, update the timeTaken + 1.
5) Return time taken, if and only if the fresh oranges count is 0, once BFS completed, else return -1.

Edge Cases
--------------
1) If the fresh oranges count is 0, return 0.
2) Check the edge case when doing BFS the pointers are not out of bound, if indexC>=COL, indexR>=ROW, or indexR <0
or indexC < 0, or not fresh orange arr[indexR][indexV] != 1, continue.

Time Complexity: O(N2)
Space Complexity: O(N2)
"""
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges = 0
        timeTaken = 0
        queue = deque()

        rows = len(grid) 
        cols = len(grid[0]) 

        for indexRow in range(0, rows):
            for indexCol in range(0, cols):
                if grid[indexRow][indexCol] == 1:
                    freshOranges += 1
                elif grid[indexRow][indexCol] == 2:
                    queue.append([indexRow, indexCol])
        
        if freshOranges == 0:
            return 0
        
        while queue and freshOranges > 0:

            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            for index in range(len(queue)):
                row, col = queue.popleft()
                for dirRow, dirCol in directions:
                    nextRow, nextCol = row + dirRow, col + dirCol
                    if (nextRow < 0 or nextCol < 0 or nextCol >= cols or nextRow >= rows or grid[nextRow][nextCol] != 1):
                        continue
                    grid[nextRow][nextCol] = 2
                    queue.append([nextRow,nextCol])
                    freshOranges -= 1
            timeTaken += 1
        
        return timeTaken if freshOranges == 0 else -1

# Testing
grid1 = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[0,2]]
sol = Solution()
print(sol.orangesRotting(grid1))
print(sol.orangesRotting(grid2))