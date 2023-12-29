"""
Difficulty: Hard/Medium
https://leetcode.com/problems/longest-consecutive-sequence/submissions/1106937146/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Solution
--------------
In real we will look on a number and check it have a predecessor or successor, and check the start of sequence and add all consequtive successors after.
So here we should find the leftmost number or starting of sequence, while iterate through array in O(N).
As like in real how we check we add 1 to leftmost number and check is there a successor exist, and continue until sequence break.
Calculate and update the maxLength value with finding of each sequence subarray.

Illustration
----------------

    <- [1,2,3,4]           <- [100]       <- [200]
        ->  ->                  
 <------------------------------------------------------>

 So here we traverse the array in O(n) + check the successors of leftmost number when found and add 1 until sequence end so possibly n-1 atmost. O(n-1+n), so we took max as O(n).

Edge cases:
1) Array is empty then return 0.
2) check num-1 exist in set (we convert array to set for convenience), if not take it as starting of sequence.
3) Push every number sequence in an array and after seq break, push into a set.

Note:
- Out of the box, if we need to show sequence, we push the sequence in an array and add in a set.
- While at same time update the global longestSeqLen parallely.

"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    
    sequences = list() #log the sequence array we build
    maxLengthOfSeq = 0 #store max length of sequence
    nums = set(nums)
    for num in nums:
        # check is the number leftmost
        if (num-1) not in nums:
            seqArray = []
            while num in nums:
                seqArray.append(num)
                num += 1
            maxLengthOfSeq = max(len(seqArray), maxLengthOfSeq) #compare maxlength and update
            sequences.append(seqArray)

    print(sequences)

    return maxLengthOfSeq

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([300,2,400,4,1]))