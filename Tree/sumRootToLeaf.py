"""
Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

Complexity: Medium

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. 
Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.

Solution
-----------
Preorder traversal NLR, is giving the expected result here. 
Every recursion we have an edge cases where to return the value and break the recursion. (here is reach the leaf node)

Steps
------
1) We can do a DFS from root node.
2) Providing an argumens called current node and number in recursion.
3) Add the each node in NLR format, in an equation num * 10 + node.value, eg: 4 -> 0, 4*10 + 0 = 40.
4) Return value calculated in num when reached at the leaf node.

Edge cases
---------
1) If no root return 0.
2) If DFS if reached leaf node that is currentNode have no left or right, return the number.
Else we will recurse to left and right.
3) If current node is null, then return 0.
4) Once the left and right nodes completed traversal to leaf node we can add them toghether and return.

Time Complexity: O(N)
Recursion 
----------
Have two rules 
1) when to break recursion and give output to recursive call
2) where to place the recursive call and how to use the recursive value in same function.
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(currentNode, number):
            if not currentNode:
                return 0
            
            number = (number * 10) + currentNode.val
            if not currentNode.left and not currentNode.right:
                return number
            return dfs(currentNode.left, number) + dfs(currentNode.right, number)
        
        return dfs(root, 0)
    

# Testing
sol = Solution()
node = TreeNode(4)
node.left = TreeNode(9)
node.right = TreeNode(0)
node.left.left = TreeNode(5)
node.left.right = TreeNode(1)
print(sol.sumNumbers(node))