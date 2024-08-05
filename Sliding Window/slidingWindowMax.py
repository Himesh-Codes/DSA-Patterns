"""
Sliding Window Maximum
Difficulty: Hard

https://leetcode.com/problems/sliding-window-maximum/description/

You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

Intuition
-----------
Keep a memory on the max value on first window so it is easy to calculate the max on upcoming window
with comparing current max (either in queue or in max variable)

Solution (Bruteforce)
----------------------
Do a sliding window keep iterating through window and find minimum element in each window.
We have window of size K so O(K) for finding min in window and we need to do that N - K times, O(N-K).
So total O(K * (N-K)) is complexity


Solution (Optimised, Dequeue) : O(N)
----------------------------------
We keep index in the queue.
Push the elements into Deque until condition where previous element in queue is greater than current.
If not pop from right until current element is greater than previous elements in queue.
This way we can say the leftmost value of dequeue is always greater in the window.
Once window slide to right pop from leftmost and add the previous window max to result array.

Edge Case
---------
1) If current left pointer index is greater than value is leftmost of queue, that means it not belongs 
to the window. So we pop left of queue. This is why we keep the index in queue.
eg: [1,5,3,4,5]
Here if we are on window |3,4,5|, and our queue is [1,4] as index value, now left == 2
So we need to pop left.

"""

import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = right = 0
        result = []
        dequeue = collections.deque()

        while right < len(nums):
            # pop until the current num is less than queue rightmost element
            while dequeue and nums[dequeue[-1]] < nums[right]:
                dequeue.pop()
            dequeue.append(right)

            # pop left in left pointer is outofbounds with respect to queue.
            if left > dequeue[0]:
                dequeue.popleft()
            
            # to add result
            if (right + 1) >= k:
                result.append(nums[dequeue[0]])
                left += 1 #for each successful addition we can move left + 1
            right += 1
        
        return result

# Testing
sol = Solution()
print(sol.maxSlidingWindow([1,-1],1))
# print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
