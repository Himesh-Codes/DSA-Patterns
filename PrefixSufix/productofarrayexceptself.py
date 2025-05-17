"""
Product of Array Except Self
Difficulty: Medium
https://leetcode.com/problems/product-of-array-except-self/description/

Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

Intuition
-----------
If we need to know the product of all other nums except self current element, we simply need to multiply
all left nums and right nums, and together multiply both left and right. (O(N2))
But to reduce O(N2) complexity we can use extra space of O(N+N) with prefix and suffix product calculation.
All number index we calculate prefix nums product and in other space suffix num product.
This will reduce O(N2) to O(N) + extra space of O(N + N), space N for pref and N for suff.

On followup without extra space, we can do by eliminate pref and suff space, use result array space to
store prefix product first keeping prefix product in a var which multiply with current num each time
and iterate back from right to left on nums keeping suffix product in a var which multiply with current num each time,
then on suffix iteration multiply with current num in index of result array essentially the prefix product for that index.

Solution(Bruteforce)
----------------------------
A brute-force solution would be to iterate through the array with index i and
compute the product of the array except for that index element. This would be an O(n^2) solution

Solution(Prefix/Suffix)
----------------------------
We can use the prefix and suffix technique. First, we iterate from left to right and store
the prefix products for each index in a prefix array, excluding the current index's number.
Then, we iterate from right to left and store the suffix products for each index in a suffix array,
also excluding the current index's number.

Solution(Prefix/Suffix Optimise)
----------------------------
The last step of iteration can be avoided by calculating and filling resultant array, while doing postfix
iteration. Initially on first iteration, we iterate from left to right to fill prefix array.
Use result array space to
store prefix product first keeping prefix product in a var which multiply with current num each time
and iterate back from right to left on nums keeping suffix product in a var which multiply with current num each time,
then on suffix iteration multiply with current num in index of result array essentially the prefix product for that index.

eg: nums = [1,2,3,4]
First pref iter: [1, 1, 2, 6]; prefix = 1,where first element 1 have no prefix so res = [1] & prefix = 1
on next where next element 2 have prefix prod 1 so res = [1, 1] & prefix = 1 * 2
on next where next element 3 have prefix prod 2 so res = [1, 1, 2] & prefix = 2 * 3 = 6
on next where next element 4 have prefix prod 6 so res = [1, 1, 2, 6] & next prefix = 24
as this is last element we are done

Next suff iter:[24, 12, 8, 6], suffix = 1, where last element 4 have no suffix so res = [1, 1, 2, 6] & suffix = 4
on next where prev element 3 have suf prod 4 so res = [1, 1, 8, 6] & prefix = 4 * 3 = 12
on next where prev element 2 have suf prod 12 so res = [1, 12, 8, 6] & prefix = 24
And so on to first element we are done.


Steps
-------
- Iterate from left to right for prefix product where pre[i] will be the prefix product.
- Iterate from right to left for suffix product where suffix[i] will be the suffix product.
- While executing the previous step after suffix[i] calculated, we fill resultant array = pre[i] * suffix[i].

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        # prefix iter
        prefix = 1
        for index in range(len(nums)):
            result[index] = prefix
            prefix *= nums[index]
        # suffix iter
        suffix = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= suffix # multiply with prefix product on result array
            suffix *= nums[index]

        return result

print(Solution().productExceptSelf([1,2,3,4]))
