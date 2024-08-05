"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Difficulty: Medium
https://leetcode.com/problems/daily-temperatures/

Similar Qn: Next greater element - https://leetcode.com/problems/next-greater-element-ii/

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

Solution (Bruteforce)
------------
For each tempurature item in the array we will traverse into it's succeding right index elements and find greater.
Worst cases might be the O(n2).

Intuition
----------
Using a stack we can backtrack previous visited temp (here we store the index), and see last element is
lesser than current temp, then popout stack until we breaks this condition.
And while pop-out alter the resultant array index with value of waiting time.

Solution (Optimised) - Stack is useful for checking, backtracking the ordered entry.
---------------
Using a stack to backtrack the previous lower tempurature.
We add visited days tempurature, and compare with previous tempuratures in stack.
On each entry of the in stack we check the last element in stack is less than current entering element, if yes, stack.pop(),
pop the last element and continue until this condition breaks, ie, last element of the stack is not greater than current temp.
Since this stack will be a monotonic decreasing, the last element in stack should be always small.
eg: Input = [73,74,75,71,69,72,76,73]
In some time the stack will be stack = [75,71, 69] and then 72 come and pop the 69, 72, because stack will be decreasing everytime.

Worst condition is monotonic decreasing order stack, that always decrease in each entry. eg: [23,22,21,20,...]

And pop the new stack element and continue until last element in stack is not greater than current entry tempurature.

Complexity - O(N)

Edge cases
----------
1) On each add we are going to add the index and and temp value in stack as dict.
2) So on each pop we can check the difference between index of pop and current tempurature as a count to add into result array.


"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stackTempurature = []

        for index in range(0, len(temperatures)):
            tempurature = temperatures[index]
            # top of stack is index -1 in python
            while len(stackTempurature) > 0 and tempurature > stackTempurature[-1]['value']:
                tempuratureInfo = stackTempurature.pop()

                if not tempuratureInfo['value'] < tempurature:
                    stackTempurature.append(tempuratureInfo)
                    break
                count = index - tempuratureInfo['index']
                result[tempuratureInfo['index']] = count
            stackTempurature.append({"index": index, "value": tempurature})

        return result


sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))