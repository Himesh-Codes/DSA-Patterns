"""
Longest Increasing Subsequence
Difficuly: Medium

Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Solution
---------
Bruteforce is using DFS with cache, for eg: [1,2,4,3].
DP in bottom approach, since the base case is last element with subsequence is 1 in length.
While traversing back in any element index we have to check right elements subsequence.
ie, max(1, 1+LIS[index+1]....., 1+LIS[index+j]), since 1 is already there if the same index element is taken, 
LIS[index+j]+1 is taken if and only if the current element arr[index] < arr[index+j]. 
And so on loop will continue until index == 1 element, first element LIS is calculated.
eg: LIS[3] = 1, since 3 is the base case
LIS[2] , longestCount = 1, since the element 4 itself is a subsequence, max(1, 1+LIS[3]) can't be taken, since
4 > 3. so LIS[2] = 1
LIS[1], longestCount = 1, max(1, 1+LIS[2], 1+LIS[3]), can be taken since 2<4 & 2<3. so LIS[1] = max(1,2,2) = 2.
And so on.

Steps
--------
1) Create DP LIS in count of N as len of array.
2) Base case LIS[N] = 1, as last element is not having any right sequence elements.
3) While iterating back in array, calculate longestSequence as max(1, 1+LIS[index+1]....., 1+LIS[index+j]), 
if and only if the current element arr[index] < arr[index+j]. 
4) Return the max(LIS), maximum subsequebce value is return, as maximum subsequence that we calculated from reverse order.


Time Complexity: O(N2), since every element will traverse to right elements.
Space Complexity: O(N)
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [0 for item in nums]
        lis[len(nums)-1] = 1

        for index in range(len(nums)-2, -1, -1):
            longestSequence = 1
            nextIndex = index+1
            while nextIndex < len(nums):
                if (nums[index] < nums[nextIndex]):
                    longestSequence = max(longestSequence, 1+lis[nextIndex])
                nextIndex += 1
            lis[index] = longestSequence

        return max(lis)

# Testing
sol = Solution()
print(sol.lengthOfLIS([0,1,0,3,2,3]))
