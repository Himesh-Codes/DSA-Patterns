"""
Permutations
https://leetcode.com/problems/permutations/description/

Difficulty: Medium

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

Intuition
----------
Recursive approach, until we find element with 1 length as return the permutation.
Idea is to have an idle element pop from first index of array,
keep a loop (until len N) to see we popout first element and create it's sub permutations.
Why loop until N becuase if n = 3 we need to shuffle the order and add idle element to end of array
ie, For [1,2,3] [2,3,1], [3,2,1], we need to find the permutations, taking 1, 2, 3 as idle elements
respectively.
So after permutation we get [2,3], [3,2] for idle num 1.
[3,1], [1,3] for idle num 2.
[1,2], [2,1] for idle num 3.
Adding idle number at end for every permute recursion we get comb results
[2,3,1], [3,2,1], [3,1,2], [1,3,2], [1,2,3], [2,1,3] is the result.

Solution
-----------
Decision tree kind of approach where we can pick one element first and other element so on.
The number of choices to pickup in one recursion will be the number of items in the array.
Once one item choosed we can remove the item and do recursion with other elements.
Our approach is a recursive backtracking solution.

Steps
---------
1) Recursion edge case is if len of num array is one do edge case 1.
2) For each and every element in array, with array positions, you can pop the element from front 'nums.pop(0)'
and get permutatation of other elements. Once poped we need to add the element to end of all permutations.
Eg: if [2,3], we pop 2 first, then [3] is only item returned with our edge case. Then we need to add 2 to end of
permutations, ie; [3,2], we pop 3, then after all we get [2,3] & [3,2].
Since the items are traverse and poped according to position, since appending will be added one more index in array
it will not pickup.
3) We do recursion inside a loop that will execute until the len(nums).
4) Append the result permutations into the array and return array in each recursion.
ie; in last recursion we get perms; [[2,3],[3,2]], in other recursion backtracked with recent permutations
we get [2,3,1],[3,2,1] and obviously [1,2,3]  will come up with 3 recursion, by appending 3 to permutation [1,2].


Edge Case
----------
1) If one value only in input return [nums[:]], with ':' we can copy all and assign into new list

Recursion 
----------
Have below rules 
1) when to break recursion (in begining) and give output to recursive call
2) where to place the recursive call and how to use the recursive value in same function, 
how many times the recursion should do for a single case.
3) how to use post recursive call operations with the output return at last of code.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]
        
        # we do this becuase the for loop range will be already calculated and avoid iteration again
        # due to appending same idle number to end of list nums
        for index in range(0, len(nums)):
            idleNumber = nums.pop(0)
            permutations = self.permute(nums)

            # append idlenumber to end of all permutations
            for permutation in permutations:
                permutation.append(idleNumber)
                # append resultant permutation to result
            result.extend(permutations)
            # append number to end of nums again to get other combimations
            nums.append(idleNumber)
        return result
