"""
Steps by Knight
Difficulty: Medium

Given a square chessboard, the initial position of Knight and position of a target. 
Find out the minimum steps a Knight will take to reach the target position.

Note:
The initial and the target position coordinates of Knight have been given according to 1-base indexing.
Your Task:
You don't need to read input or print anything. Your task is to complete the function minStepToReachTarget() which takes the initial position of Knight (KnightPos),
the target position of Knight (TargetPos), and the size of the chessboard (N) as input parameters and 
returns the minimum number of steps required by the knight to reach from its current position to the given target position or return -1 if its not possible.

Expected Time Complexity: O(N2).
Expected Auxiliary Space: O(N2).

Example 1:

Input:
N=6
knightPos[ ] = {4, 5}
targetPos[ ] = {1, 1}
Output:
3
Explanation:
Knight takes 3 step to reach from 
(4, 5) to (1, 1):
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1).

Constraints:
1 <= N <= 1000
1 <= Knight_pos(X, Y), Targer_pos(X, Y) <= N

Solution
---------
BFS solution, with visited array.
1) Start and End point should be considered as {x-1, y-1}, {a-1, b-1}, 
since the coordinates in chess board are considered as array matrix.
In which the array size is given as argument "N", ie, matrix of NxN.
2) Add starting point into the queue, 
while pop the items in current queue add it's adjacent coordinates, 8 positions into adjQueue,
 if and only if it is not visited. 
3) Calculate the step+= 1 and swap with current queue once loop is completed, 
when one queue is completely poped, if and only if targetFound is False.
4) Once target reached break the loop and update targetFound.
"""
from typing import List

class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos: List[int], TargetPos: List[int], N) -> int:
        steps = 0
        targetFound = False
        startX, startY = KnightPos[0]-1, KnightPos[1]-1
        targetX, targetY = TargetPos[0]-1, TargetPos[1]-1
        col = row = N

        directions = [[-2,-1], [-2,1], [-1,2], [1,2], [2,-1], [2,1], [1,-2], [-1,-2]]
        queue = [[startX, startY]]
        visited = set()
        # set items should be hashable sets
        visited.add((startX,startY))

        while queue:
            adjQueue = []
            for _ in range(len(queue)):
                indexX, indexY = queue.pop(0)
                if targetX == indexX and targetY == indexY:
                    targetFound = True
                    break
                for moveX, moveY in directions:
                    newX, newY = indexX + moveX, indexY + moveY
                    if (newX, newY) not in visited and newX >= 0 and newY >= 0 and newX < row and newY < col:
                        adjQueue.append([newX, newY])
                        visited.add((newX, newY))
            if not targetFound:
                steps += 1
                queue = adjQueue
        
        return steps if targetFound else -1

# Testing
sol = Solution()
print(sol.minStepToReachTarget([4,5], [1,1], 6))