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
----------
Recursive approach in 2 possibilities every time.
1 when open bracket count is less than N we can add "(" and do recursion.
2 when open bracket > close bracket we can add ")" at end of array.
Imagine once we recurse until our condition 1 breaks open < N, 
we append ")" until condition 2 breaks. So our first combination will be N number of open bracket 
and N close bracket.
Eg: N = 3 first combo will be ((())), becuase our recursion break condition is N = open = closed.

Then backtrack and pop out close and open bracket become 2 on backtrack and add other combination (()()).
(Draw on paper and see recursion flow like a graph)
eg: N = 2

Recursion illustration:

start with open        here we can't add close since open count < close, since last step open == close (1)
        "(" --> ")" --> "(" --> ")"
         |
         V
        "(" -- > ")" --> ")"
dfs last step is 
2nd open bracket then
we met open > n
so add close until open 
is greater than close.
After 2nd bracket added 
if we recurse open == close = n
so add to comibination.         

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