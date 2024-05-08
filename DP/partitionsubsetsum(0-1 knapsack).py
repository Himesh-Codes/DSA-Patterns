"""
Partition Equal Subset Sum
Difficulty: Medium

Given an integer array nums, return true if you can partition the array into two subsets such that the
 sum of the elements in both subsets is equal or false otherwise.


Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Solution
---------------
The 0-1 knapsack method, means the array items can be used either 0 times or 1 time.
Brute force is recurse through all possible ways and find the sum to be target, in every step either choose a number
or not choose possibility there this will run on O(2^N) complexity.
But since the one problem step is calculated we don't want to recalculate the similar step again
Let's say if we choose 1->5 and in other step we choose 5->1 both have sum of 6 and 5 more needed to achieve our target.
So we can use DP over here.

Steps
-------
1) We have to identify how to make it equal partition that is sum(arr) should be even and sum(arr) // 2 is our target.
Add zero to the sumSet since the base condition of not choosing any item.
2) Now everytime if we pick one item we can add it into our pick sack (set) or not. 
Add it into a set when a number is picked, iterate through whole array and add the sum and number to set.
3) For each number iterate through the set and add the sum with current number and each other precalculated sums.
4) If the set contains a target number return true else false.

Edge cases
----------
1) If sum of array is not even return false
2) If the sumSet contains the target ie, sum(arr) // 2, after each calculation immediately return false.

Time Complexity: O(N*sum(arr))
Space Complexity: O(sum(arr)), max of the total sum of array will be the length.
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arraySum = sum(nums)
        if arraySum % 2 == 0:
            dp = set()
            dp.add(0)

            target = arraySum // 2

            for num in nums:
                if num == target: return True
                currentDp = set()
                for sumnum in dp:
                    total = sumnum + num
                    if total == target: return True
                    currentDp.add(sumnum + num)
                    currentDp.add(sumnum)
                currentDp.add(num)
                dp = currentDp

        return False
    

#Testing
sol = Solution()
print(sol.canPartition([1,5,11,5]))
print(sol.canPartition([1,2,3,4,5]))