"""
Search in Rotated Sorted Array
Difficulty: Medium

https://leetcode.com/problems/search-in-rotated-sorted-array/description/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

Solution
----------
Search in sorted array we can use the binary search, since the structure will be of the binary tree.
Best practice: Use the same input array to validate the different edge cases, with considering different element position.
ie; here we can see [4,5,6,7,0,1,2] that mid value as 6, and see mid value if 1.

Steps
--------
[4,5,6,7,0,1,2] - input 
1) Check the mid we are checking is in left sorted (big) [4,5,6,7] array or right sorted (small) array [0,1,2]. 
ie, check mid >= left, if mid =1, left is 4 so we know, 1 is in right sorted array.
2) if in left sorted array, see target > mid or target < left (if 0 is target), move right, thatis left = mid + 1
else move left, thatis right = mid-1 (imagine target 6, ie, target > left)
3) if in right sorted array, see target < mid (imagine 0 is target 1 is mid) 
or if target > right (imagine 5 is target and we are in right array with mid = 1), move left,ie; right = mid -1
else move right, thatis left = mid + 1

Edge Cases
----------
1)If mid  not equal to target, we need to check two conditions and recursive accordingly
2) If mid > target and right >= target, then left = mid+1
3) If mid < target, left <= target, then right = mid-1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findInRotatedArray(left, right, target):
            if left <= right:
                mid = (left + right) //2
                if nums[mid] == target:
                    return mid
                # left sorted array (large num array)
                if nums[left] <= nums[mid]:
                    # the leftmost element is greater than target in leftmost large arr then probability only in rightarr
                    if target > nums[mid] or nums[left] > target:
                        return findInRotatedArray(mid+1, right, target)
                    else:
                        return findInRotatedArray(left, mid-1, target)
                # right sorted array (small num array)
                else:
                    # the right element is less than target is rightmost small array then probability only is leftarr
                    if target < nums[mid] or nums[right] < target:
                        return findInRotatedArray(left, mid-1, target)
                    else:
                        return findInRotatedArray(mid+1, right, target)
            return -1
    
        return findInRotatedArray(0, len(nums)-1, target)
# Testing
sol = Solution() 
print(sol.search([4,5,6,7,0,1,2], 0))