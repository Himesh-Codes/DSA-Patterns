"""
Circular Array Loop
Difficulty: Medium
https://leetcode.com/problems/circular-array-loop/description/

You are playing a game involving a circular array of non-zero integers nums. 
Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.

Since the array is circular, you may assume that moving forward from the last element puts 
you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index 
sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1

Return true if there is a cycle in nums, or false otherwise.

Example 1:
Input: nums = [2,-1,1,2,2]
Output: true
Explanation: The graph shows how the indices are connected.
 White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are 
white (jumping in the same direction).

Example 2:
Input: nums = [-1,-2,-3,-4,-5,6]
Output: false
Explanation: The graph shows how the indices are connected. 
White nodes are jumping forward, while red is jumping backward.
The only cycle is of size 1, so we return false.

Example 3:
Input: nums = [1,-1,5,1,4]
Output: true
Explanation: The graph shows how the indices are connected. 
White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, 
it has a node jumping forward and a node jumping backward, so it is not a cycle.
We can see the cycle 3 --> 4 --> 3 --> ..., 
and all of its nodes are white (jumping in the same direction).

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
nums[i] != 0

Solution(Fast/Slow Pointer)
----------------------------
Cycle is found if and only 3 conditions satified.
1) Cycle Sequence length should be greater than one.
2) Sequence should be either all positive or all negative.

Since array is circular if value arr[i] + i > len(arr), reminder we start from 0 and move front.
Same as if arr[i] + i < 0, reminder we start from end arr[n-1] and move back.
Common equation is newIndex = arr[i] + i % n, 
if newIndex < 0, newIndex = n - (arr[i] + i % n), since negative number we move back from end.

Steps
-------
- We find the loop using fast and slow pointer, for each element (non visited).
- If found calculate length and from fast and slow pointer intersect index, keep a count.
- While taking length validate sequence contains only +ve or only -ve.
- While taking length assign '0' as for visited positions, since in question it states "nums[i] != 0".

"""
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def indexCalculate(index):
            newIndex = index % n
            if newIndex < 0:
                return n - newIndex
            return newIndex
        
        def findLoop(fast, slow):
            if fast == slow:
                return fast
            while fast != slow and fast < len(nums):
                slow = indexCalculate(slow + nums[slow])
                fastStep = indexCalculate(fast + nums[fast])
                fast = indexCalculate( fastStep + nums[fastStep])
                if fast == slow:
                    return fast
            return -1
        
        def validateBothPosOrNeg(prev, current):
            if prev < 0 and current < 0:
                return True
            if prev > 0 and current > 0:
                return True
            else:
                return False

        def findLengthAndValidateCycle(head):
            index = indexCalculate(head + nums[head])
            previousValue = nums[head]
            nums[head] = 0
            length = 1
            while index != head:
                length += 1
                currentValue = nums[index]
                nums[index] = 0
                # see both are +ve or -ve
                if not validateBothPosOrNeg(previousValue, currentValue):
                    return False
                previousValue = currentValue
                index = indexCalculate(index + previousValue)
                
            if length > 1:
                return True
            return False

        for index in range(len(nums)):
            if nums[index] != 0:
                slow = index
                fast = indexCalculate(index + nums[index])
                loopIndex = findLoop(fast, slow)
                if loopIndex >= 0:
                    if findLengthAndValidateCycle(loopIndex):
                        return True
        return False
                
# Testing
sol = Solution()
print(sol.circularArrayLoop([1,-1,5,1,4]))
print(sol.circularArrayLoop([-1,-2,-3,-4,-5,6]))
print(sol.circularArrayLoop([2,-1,1,2,2]))