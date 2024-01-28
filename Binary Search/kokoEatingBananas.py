"""
Koko Eating Bananas
Difficulty: Medium
https://leetcode.com/problems/koko-eating-bananas/description/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

Solution
----------
Pattern identified: find minimum in a sorted array, here the banana-per-hour time array with specific condition.
We can see the h (hours) will be greater than the bananan pile array length, so if the koko eat the maximum pile count 
(11 here) he can finish all piles in given time.
[3,6,7,11], h = 8, if banana per hour is 11 it can finish all the banana in 4 hours, but catch here is we have to find
the minimum speed, so we have a sorted array [1,2,3.....,10,11].
 
Steps
--------------
1) Binary search on the eatspeed array, 
2) On each iteration see the banana per hour speed can complete all piles in banana array by 
traversing on all of this items, bounded by the time limit.
3) Once iterate until hour ends, and see the last finished-pile-index is same as last index of array. 
If yes then check he can finish in lesser eatspeed. 
If can't finish check greater eatspeed.
4) Keep a minimum speed noted, so if we get that until the array is done with binary search.

Edge cases
-----------
1) Each hour Koko eat only one pile, so here the Koko like to eat slow if he can finish all pile in given time.
Let's take an example if pile contains 6 bananas, so if eating speed is 4 banana per hour for next 2 hours he eat that.
2) Optmise memory, without constructing a list of each pile use the left and right as point, initially left will be 1, and right will be max(piles)

"""

from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimumSpeedNeeded = float('inf')
        # memory optimised using the left as minimum speed of 1 and right as max speed of max number in pile
        left, right = 1, max(piles)

        while left <= right:
            mid = (left+right)//2
            pileIndex = 0
            hours = h
            while hours > 0 and pileIndex < len(piles):
                hours -= ceil(piles[pileIndex]/mid)
                pileIndex += 1

            if hours >= 0 and pileIndex == len(piles):
                minimumSpeedNeeded = min(minimumSpeedNeeded, mid)
                right = mid-1
            else:
                left = mid+1

        return minimumSpeedNeeded
    
# Testing
sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))
print(sol.minEatingSpeed([30,11,23,4,20], 5))
print(sol.minEatingSpeed([30,11,23,4,20], 6))