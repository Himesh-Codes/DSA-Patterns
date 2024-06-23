"""
Difficulty: Hard

https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


            _____               _____
    ____    |   |____           | 3  |
    | 2 |   |3  | 2 |           |    |
    |   |   |   |   |           |    |
--------------------------------------------

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Solution 1 - Memory O(N)
------------
Use a memoization table to add maxLeft when looking in a position and maxRight in a position.
So the capacity will be min (maxLeft, maxRight) - height of current elevation
Eg: [4,2,0,3,2,5], index = 1, maxLeft = 4, maxRight = 5, so, 4-2 = 2 is the capacity.
But in let's say [4,5,0,3,2,5] index = 1, maxLeft = 4, maxRight = 5, so, 4-5 = -1 is the capacity, so not added into trapcapacity.

Solution 2 (optimal)
------------
Two pointers start at both ends, calculate the capacity on the way.

Steps
-------------
1) We need to iterate both pointers until both of the elevations are non zero numbers.
2) Then we find capacity elevation is overflow, that is until Left > Right or Right < Left condition breaks, we calculate the capacity with each block, 
3) If Left < Right we iterate LeftIndex++ , and vice versa, so we get a container capacity.
4) capacity = (currentBlock - smallest Among Left Or Right)

5) Until LIndex == RIndex, we do the above operations.

Illustration with example:
[4,2,0,3,2,5]

L=4 , R=5, so step 1 is completed both are non zero
while L<R: (since L is smaller)
Iterate L, capacity => 4-2 + 4-0 + 4-3 + 4-2 = 9
Now Lindex == RIndex, so total 

Complexity : O(N)

Edge cases
--------------
1) If not able to find non zero elevation either in one pointer or both, trap capacity is zero
2) If Left and Right elevation value is equal, we can choose any pointer to iterate. Here we iterate Right.
3) While iterating we need to see the container value is greater than zero, example L=5, R=2, currentBlock = 4, 
capacity = 2-4, but we can't store anything, so we ignore this addition.
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        trapCapacity = 0
        leftIndex = 0
        rightIndex = len(height) - 1

        # while both elevations are non zero
        while height[leftIndex] == 0 and height[rightIndex] == 0 and leftIndex != rightIndex:
            if height[leftIndex] == 0 : leftIndex += 1
            if height[rightIndex] == 0 : rightIndex -= 1
        
        while leftIndex != rightIndex:
            if height[leftIndex] < height[rightIndex]:
                lowElevation = height[leftIndex]
                leftIndex += 1
                while lowElevation > height[leftIndex] and height[leftIndex] < height[rightIndex]:
                    trapCapacity += lowElevation - height[leftIndex]
                    leftIndex += 1
            else:
                lowElevation = height[rightIndex]
                rightIndex -= 1
                while lowElevation > height[rightIndex] and height[rightIndex] < height[leftIndex]:
                    trapCapacity += lowElevation - height[rightIndex]
                    rightIndex -= 1
            

        return trapCapacity


# Test cases
sol = Solution()
print(sol.trap([5,4,1,2]))
print(sol.trap([4,2,0,3,2,5]))
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))