"""
Binary Tree Right Side View
Difficulty: Medium
https://leetcode.com/problems/binary-tree-right-side-view/description/

Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Solution
---------
 * Have 2 Approaches
 * 1- Is using a queue and doing BFS (Time Complexity: O(n2), Space Complexity: O(N))
 * 2- Doing recursion in order right() and left(), so after right the recursion go to right,
 * If both all null return to root parent. 
 * (Time Complexity: O(n), Space Complexity: O(1)), check in Java solution.

Using the BFS traversal of the tree but in a tricky way.
BFS traversal is the level order traversal in tree.

Steps
-------
1) For BFS traversal we create a queue and add the base case, root into queue.
2) We add the left element and then right element of node in the order, left, right to queue.
We add the rightmost element in queue always to the result array.
3) After an rightmost element in queue is removed everytime, see any elements are there in left side of queue.
4) If yes pop them one by one, while pop each element add it's children (if exist) into queue, inorder of left, right.
5) Do this until the queue is empty and reached last leaf node of tree.

eg:         1
        2       3
            5       4
                7

Here the output should be: [1,3,4,7] as the right view
So we add the queue = [1], then iterate in queue until queue is empty.
Add the rightmost element in queue now it's 1, res = [1]
Then pop the queue in other loop, from leftmost element in queue until rightmost.
pop 1, and add children in order left, right, queue = [2,3], add right most into res = [1,3]
Then pop the queue in the left to right, pop 2 and add it's child 5, pop 3 finally and add 4, so res = [5,4]
Atlast the queue = [7] and pop 7 and find no children, and now queue is empty.
res = [1,3,4,7]

Edgecases
--------
1) If root is None, return empty array [].

Time Complexity: O(N2)
Space Complexity: O(N)

Double ended queue solution:  https://www.youtube.com/watch?v=d4zLyf32e3I
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        queue = [root] #base case is add root in queue.

        while len(queue) > 0:
            rightmostelement = queue[len(queue)-1]
            result.append(rightmostelement.val)
            childqueue = []
            for node in queue:
                if node.left: childqueue.append(node.left) 
                if node.right: childqueue.append(node.right) 
            queue = childqueue
        
        return result
    
# Testing
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
root.left.right.right = TreeNode(7)
sol = Solution()
print(sol.rightSideView(root))