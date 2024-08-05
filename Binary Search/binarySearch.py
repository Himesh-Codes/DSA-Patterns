"""
Binary Search
https://leetcode.com/problems/binary-search/description/
Complexity: Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

Intuition
---------
On binary search we use left and right pointers divide and move according to mid point value.
If target greater than mid value go right. left = mid+1
If target less than mid value go left. right = mid-1

Solution
----------------
Since array is sorted we use the divide and conquer approach is basic for binary search
So as we know "log N" is the number of time a number N can be divided by 2. That's how this approach is O(logn)
time complexity.

Steps
-------
1) Use pointers like left, right. Since the question need us to return the exact index of the item.
2) Find the mid with respect to left and write pointers on every recursion. left+rigth/2.
3) Check the target value is less or greater than the mid, adjust left of right pointer in order to reduce 
the coverage of the array.
4) Check and reduce the array coverage pointer until the mid item is a single element.

Complexity: O(logn)

"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(left, right, target):
            if left <= right:
                mid = (left + right)//2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    return find(mid+1, right, target)
                elif target < nums[mid]:
                    return find(left, mid-1, target)
            return -1
        return find(0, len(nums)-1, target)
    
sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))
print(sol.search([-1,0,3,5,9,12], 2))
print(sol.search([2,5], 0))
print(sol.search([-1,0,3,5,9,12], 13))