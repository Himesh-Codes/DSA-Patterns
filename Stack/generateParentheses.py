"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

https://leetcode.com/problems/generate-parentheses/

Difficulty: Medium
 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

Intuition
-----------
We know how much bracket should be there, so either you can add open bracket or close bracket.
Close bracket can only added if open bracket count > closed bracket count.
eg:   Bracket count = 3

                    (
                /      \
open =2,close=1(        )       open = 1, closed =1 , now only one option is adding open
now one we have/ \       \
2 options      (  )       (

According to the open bracket count in the stack you can add close bracket.
As per above we can see two possible ways according to open, close bracket count.
open > closed then we can return and add brackets into result.

Using recursion: 
We can check if opencount < n, add open bracket to stack, do recursion
At this same point we have other option to add close bracket into stack, if anly only if
open>closed count.
So while above opencount increasing recursion completed, 
on backtrack remove the existing "(" from stack and add our other option ")" and recurse.

Solution 1
--------------
Using recursion, stack.

We will use recursion to go with different combinations, and stack to validate the parenthesis entry.

Edge cases
------------
1) If n = 0, return [], an empty array.
2) If openCount of parentheses is less than 'n', we can append "("
3) If openCount > closedCount of parentheses  we can append ")"
4) We use a global stack to append parentheses, and pop the stack since the stack is global
5) If openCount and closedCount is equals n, then we can append it to combination result.
"""
from typing import List
import copy

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        stack = []
        
        if n == 0:
            return []

        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
               combinations.append("".join(stack))
               return

            if openCount < n:
               stack.append("(")
               backtrack(openCount+1, closedCount)
               stack.pop()

            if openCount>closedCount:
                stack.append(")")
                backtrack(openCount, closedCount+1)
                stack.pop()
        
        backtrack(0, 0)

        return combinations

# test cases
sol = Solution()
print(sol.generateParenthesis(3))