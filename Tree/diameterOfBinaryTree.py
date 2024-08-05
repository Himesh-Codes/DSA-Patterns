"""
Diameter of Binary Tree
Difficulty: Easy

https://leetcode.com/problems/diameter-of-binary-tree/description/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

Intuition/Approach
-------------------
If we know the diameter of the leaf node that is 0, (left -1 + right -1 + 2 edges).
Diameter is the left node length + right node length + 2 (edges to left and right child).
Once lower part is calculated we need to calculate upper part, doing DFS and track back.
Always see update the maxDiameter always one DFS completed on left and right node.

But note that either maximum in left / right we can take from current node,
so take left / right length and add 1 (includes current node) to return len on back track.
After root element you will get maxDiameter in global variable return.

Solution
--------------
Longest path between two node is the diameter of the tree.
We can do a DFS and do a reverse order calculation, ie; from the leafnode count the height.
So once the DFS of a node left and right branch completed we can get max height among left and right.

Step
--------
1) Do DFS recursion for a node right and left branch.
2) If node is None return -1, so that is leaf node height will be calculated left/right+1 is zero.
3) Add height will be 1 + max(left, right), so that the parent node edge will be also calculated,
 since this is the maximum height return this height to parent node recursive call.
4) use a maxdiameter global so max(maxdiameter, left+right+2), will be answer. We add 2 since the parent edge 
need to calculate
UnboundLocalError: cannot access local variable 'maxDiameter' where it is not associated with a value, so in python 
we add it as an array.
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
    
        def dfs(root):
            if not root:
                return -1
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            maxDiameter[0] = max(maxDiameter[0], leftHeight+rightHeight+2)

            return max(leftHeight, rightHeight) + 1
        
        dfs(root)
        return maxDiameter[0]