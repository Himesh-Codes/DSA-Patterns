from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

nums = [1,2,4,5,1]
target = 7

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

 Solution
 ------------
 Hashmap used to keep memorize the previous visited numbers and it's index
 If the target minus the number matches anything in hashmap then print indexes [i,j]

 Edge cases:
    execute the match 

 Notes:
    1. hashmap "key" is number itself and value is index.



https://leetcode.com/problems/two-sum/submissions/

"""

def twoSum (nums: List[int], target: int):
    sumMap = {}
    for index in range(0, len(nums)):
        if (target - nums[index]) in sumMap:
            return [sumMap[target - nums[index]], index]
        if nums[index] not in sumMap:
            sumMap[nums[index]] = index

print(twoSum([1,2,4,5], 7))
print(twoSum([3,2,4], 6))