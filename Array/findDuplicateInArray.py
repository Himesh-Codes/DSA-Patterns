"""
Find All Duplicates in an Array
Complexity: Medium
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Solution
---------
1) Use "in" operator takes O(N)
2) Once and array index is iterated we will see the next index to end of the list subarray,
 array[index+1:N] and use in operator to find the element in future index or not.
3) The liner time complexity will be incresed as O(N) iterate in array + O(N) search in subarray.

Solution (Optimised)
---------
1) As constraint state, the n as the length of array, 
it is for sure that number will be present atleast (1 <= nums[i] <= n).
 Leverage the use of same array space and use the technique "Negative the element".
2) Here trip is to use the array number value as index and make it negative. 
when an element is traversed, we need to see element visited, 
so we can leverage use of array index and make the element negative.
ie, if num is 3 in array at current traversal we make nums[3-1] *= -1 multiple the element by -1 
that makes the index element as negative.
And when same element occured in future we see the same index here 3 comes second time 
and since already nums[3-1] is negative we can add it is duplicate.
3) Everytime before we compare we take the positive value of element only,
 since the possibility of element become negative on above step is there.
We can use abs here.
4) Iterate until the element in array is traversed (we can use range to define
 the original array length).
"""
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                result.append(num)
            else:
                nums[num-1] *= -1
        return result
    

# Testing
sol = Solution()
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))