"""
Evaluate Reverse Polish Notation

Difficuly: Medium
https://leetcode.com/problems/evaluate-reverse-polish-notation/

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

Solution
---------
Use a stack to store the operation flow, while iterating through the array from the beginning.

Steps
------
1) Iterate from begining to the end, push numbers to a stack
2) If an operator coming up pop the last two numbers, then push the answer to stack, continue until end of the array.
3) Use eval() for expression evaluation.
4) Final number in stack after array traverse is completed is the answer.
eg: ["4","13","5","/","+"] => On iteration push 4 to stack, push 13, push 5, then operator "/" came,
 then do calculation 13/5 in math floor, push answer to stack, then operator +, pop answer of 13/5 and 4, then do calculation,
 13/5 + 4 = 6.
 
Complexity: O(N)
----------

Edge cases
-----------
1) If substracts we need to take the num2 (second pop in stack, ie is first number we traversed) - num1
2) If divide we do num2 / num1, and to round off to zero, or previous number we use int() api of python.
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        itemStack = []
        for item in tokens:
            if item in ["+", "-", "*"] and len(itemStack) > 0:
                numOne = itemStack.pop()
                answer = eval(itemStack.pop() + item + numOne)
                itemStack.append(str(answer))
            elif item == '-':
                numOne = int(itemStack.pop())
                numTwo = int(itemStack.pop())
                itemStack = eval(numTwo - numOne)
            elif item == "/":
                numOne = int(itemStack.pop())
                numTwo = int(itemStack.pop())
          
                answer = int(numTwo / numOne)
                itemStack.append(str(answer))
            else:
                itemStack.append(item)

        return int(itemStack[0])
    
# test cases
sol = Solution()
# print(sol.evalRPN(["4","13","5","/","+"]))
# print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(sol.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]))