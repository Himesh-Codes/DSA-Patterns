"""
Merge Intervals

Difficulty: Medium
https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
 
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Intuition
-----------
Visualize the nums in a line what we do is find overlaping lines in intervals and merge into a longer line.
Here we can use bracketisation method were each interval limit lower & higher bound in a bracket, when new interval came, we compare with bounds
either update higher bound with current end of interval in start of current interval is in bracket b/w lower and higher bound.

Solution(Bruteforce) O(N2)
----------------------------
If the intervals are unsorted eg: [[1,5], [14,16], [3,4]]
When iterate through every interval essential need iterate through all other interval and see any merging interval can be made.
Then append to result array

Solution(Optimised) O(N + NlogN), Space: O(1)
----------------------------
Sort the interval array based on first element or push into heapq and pop gives small interval first.
Then it is just a matter to keep currentstart and currentend, on every interval start and end see if it can be merged, how?
See the currentend > start of interval if yes merge by update currentend by max(end, currentend). Continues until it breaks?
When currentend < start, push into result = [currentstart, currentend], then new iter with currentstart = start of interval now, 
currentend = end of interval.
eg: [[1,5], [14,16], [3,4]] => sorted [[1,5], [3,4], [14,16]]
currentstart = 1 currentend = 5, on next interval 3 < currentend 5, so merge currentend = max(4, 5) = 5
When 14 > currentend 5, push into res = [[1,5]]
=> res = [[1,5], [14,16]]

Solution(Optimised Greedy) O(N+M), Space: O(M)
----------------------------
We came into this approach to reduce time complexity, but as greedy can be complex at time but reduce complexity is optimal cases.
Explained in *resources/Merge interval greedy.png

"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res =  []
        intervals.sort(key=lambda pair: pair[0]) #O(N Log N)

        current_start, current_end = intervals[0]
        for start, end in intervals: #O(N)
            if start <= current_end:
                current_end = max(end, current_end)
            else:
                res.append([current_start, current_end])
                current_end = end
                current_start = start
        res.append([current_start, current_end])

        return res

    def mergeGreedy(self, intervals: List[List[int]]) -> List[List[int]]:
        res =  []
        max_value = max(interval[0] for interval in intervals)

        num_line = [-1] * (max_value + 1)
        for start, end in intervals:
            if num_line[start] != -1:
                num_line[start] = max(end, num_line[start])
            else:
                num_line[start] = end
        
        current_start = -1
        current_end = -1
        for index in range(len(num_line)):
            if num_line[index] != -1:
                start = index
                end = num_line[index]
                if current_start == -1:
                    current_start = start
                    current_end = end
                else:
                    if start <= current_end:
                        current_end = max(end, current_end)
                    else:
                        res.append([current_start, current_end])
                        current_end = end
                        current_start = start
        res.append([current_start, current_end])

        return res
    
print(Solution().mergeGreedy([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,5], [14,16], [3,4]]))
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))