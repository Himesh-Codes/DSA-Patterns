"""
Majority Element (Boyer-Moore Majority Vote Algorithm)
Difficulty: Easy

https://leetcode.com/problems/majority-element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

For example, the majority element is 2 in array {2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2}.


Solution
----------
Naive approach is keep a hashmap and update count, once a count of element is greater than n/2
return that element.

Optimised Solution: Boyer-Moore Majority Vote Algorithm

Intuition
----------
Imagine like a Election Voting for leading candidate we reduce count if opposition candidate got 1 vote,
also opposition candidate became leading candidate if vote is 0 for first candidate and opposition got 1
now.

If an element is present more than n/2, if we keep a COUNTER added +1 if same element found compare to
previous we found TRACK ELEMENT.
and -1 COUNTER if we found mismatch.
If the COUNTER becomes 0 or initially zero we make current element as TRACK ELEMENT.

Explaination: When the elements are the same as the candidate element, votes are incremented 
whereas when some other element is found (not equal to the candidate element), we decreased the count. 
This actually means that we are decreasing the priority of winning ability of the selected candidate, 
since we know that if the candidate is in majority it occurs more than N/2 times and the remaining elements 
are less than N/2. We keep decreasing the votes since we found some different element(s) 
than the candidate element. When votes become 0, this actually means that there are the equal  number 
of votes for different elements, which should not be the case for the element to be the majority element. 
So the candidate element cannot be the majority and hence we choose the present element as the candidate 
and continue the same till all the elements get finished.

Steps
-------
1) declare counter = 0 and candidate as -1
2) If we found the counter is 0 make candidate as current num, since it can be a potential candidate.
And increase count.
3) If mismatch found we do counter - 1 and reducing the scope of winner candidate vote.
4) If a match again found with candidate increase counter + 1

Edge cases
----------
Imagine a scenario where [2,1,2,3,2]
Here everytime counter increse + 1 and decrease -1, but potential candidate is 2. And is the result.
Also same count different order [2,2,1,3,2]
Here after second 2 counter == 2 and next 1,3 we do decrement of counter, that became 0.
Since counter is equal to 0 we assign last 2 as candidate and winner.
This is because in question states assume there will be one winner always.

IF NOT THIS CASE ONCE WE FOUND A WINNER WE NEED TO DO A O(n), TRAVERSAL TO FIND THE WINNNER IS REALLY
HAVE A COUNT OF N/2.
Because eg: [2,2,1,3,4], in this case 2 is not count of n/2, but as per our algo
after 3 counter == 0 and when 4 came we take it as candidate and return.
But really 4 is only count 1.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidateElement = -1
        counter = 0
        for num in nums:
            if counter == 0:
                counter += 1
                candidateElement = num
            elif candidateElement == num:
                counter += 1
            else:
                counter -= 1
        return candidateElement

# Testing
sol = Solution()
print(sol.majorityElement([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]))