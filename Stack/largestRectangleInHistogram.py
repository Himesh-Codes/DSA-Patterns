"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
 return the area of the largest rectangle in the histogram.

Difficulty: Hard
https://leetcode.com/problems/largest-rectangle-in-histogram/

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

Solution
------------
Using the STACK as a way find how much a reactangle is extensible and define boundary.
Variables used, STACK({index, value}), MAX_AREA.

Steps
---------
1) On traversing each item in array we are looking for a scope until what limit, the specific block can be
extended.
2) Push all the blocks into stack, with checking some edge cases mentioned below. The block details are pushed like
{INDEX, VALUE}, Index is for calculating the area accordingly until which block index the block is extended.
3) Look on the current block and previous blocks in stack, pop from stack until condition breaks.
4) On each pop calculate the area, (currentIndex - popedItemIndexInStack) x height.
5) Update the max_area when every time area calculated.
6) Atlast the all items in stacks are poped in LIFO order and see the area calculated like 
(len(array) - currentpopIndex) x height, and compare with the max_area and update.

Edge Cases
-----------
1) If current block is less than previous blocks, pop until the condition changes to current block > previous blocks in
stack.
2) If we pop the larger blocks from stacks when current block < previous blocks on stack, remember the possibility of
current block can be contained in popped previous stacks since current block less than previous blocks.
Eg: [2,1,5,6,2,3], here if we traverse '2' in index 4, we pop 6 and 5 respectively from stack, so we can see '2' is
smaller than 5,6 so this block can be contained in 6 & 5 position. So max index it can reach is 2, so when adding
'2' block into stack, add like {last_poped_index, height}.


Complexity
----------
Time: O(N)
Space: O(N), since the stack is proportionate to the input array size
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        stack = []
        for index in range(0, len(heights)):
            last_index = index
            if len(stack) > 0:
                previous_block_in_stack = stack.pop()
                stack_not_empty = True
                while (stack_not_empty and previous_block_in_stack["value"] > heights[index]):
                    area = (index - previous_block_in_stack["index"]) * previous_block_in_stack["value"]
                    max_area = max(area, max_area)
                    last_index = previous_block_in_stack["index"]
                    if len(stack) > 0: 
                        previous_block_in_stack = stack.pop()
                    else:
                        stack_not_empty = False
                if stack_not_empty: stack.append(previous_block_in_stack) 
            stack.append({"index": last_index, "value": heights[index]})
        
        while (len(stack) > 0) :
            block_in_stack = stack.pop()
            area = (len(heights) - block_in_stack["index"]) * block_in_stack["value"]
            max_area = max(area, max_area)

        return max_area

# Test cases
sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))