"""
Binary Tree Maximum Path Sum
Difficulty: Hard

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
has an edge connecting them. A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

Solution (Kadane's Algo)
------------------------
Keep MAX_SO_FAR (initial value as -ve float("inf")) and SUM (0).
We do DFS on tree left and right, on reaching each node we update the MAX_SO_FAR variable.
And calculate the SUM and return the value to parent.

MAX_SO_FAR is the total path included left and right tree, included current node.
SUM is the total sum either on left path sum or right path sum added to current node.

Eg:                     11

                9               20

                            5           7

                        -10     5

Doing DFS we will reach the root nodes.
Here from leaf node on -10, we go down and return 0 from right and left child null node.
So MAX_SO_FAR = -10, SUM = -10.

Same leaf node 5, have got return 0 from right and left child null node.
So MAX_SO_FAR = 5, SUM = 5.

Parent node 5 of both, we get SUM = -10 from left and SUM = 5 from right.
SUM = max(node, node+leftsum, node+rightsum), here SUM = (5, 5+ -10, 5+5) = 10
MAX_SO_FAR = max(MAX_SO_FAR, node, node+leftsum+rightsum, node+leftsum, node+rightsum), 
here MAX_SO_FAR = (5, 5, 5+ -10 + 5, 5 + -10, 5+5 ) = 10

Similarly 7,  MAX_SO_FAR = 10, SUM = 7.

In node 20, we get SUM = 10 from left and SUM = 7 from right.
SUM = max(node, node+leftsum, node+rightsum), here SUM = (20, 20+10, 20+7) = 30
MAX_SO_FAR = (MAX_SO_FAR, node, node+leftsum+rightsum, node+leftsum, node+rightsum), 
here MAX_SO_FAR = (10, 20, 20+10+7, 20+10, 20+7) = 37.

Similarly 9,  MAX_SO_FAR = 9, SUM = 9.

And last 11 have, leftsum = 9, rightsum = 30
MAX_SO_FAR = (37, 11, 11+9+30, 11+9, 11+30)  = 50
SUM = (11, 11+30, 11+9) = 44.
Once reached root we return max so far (MAX_SO_FAR).

Intuition / Approach
---------------------
DFS approach until leaf node and take decision in bottom up approach backtracking.
We can leverage on Kadane's algo, keep max_so_far global and update on every backtrack.
In each node our decision would be according to current_sum.
current_sum can be maximum of either left sum or right sum, becuase we can return only one path sum.
or current_sum can be current node, leverage on Kadane's if both right and left sum less than current node.
No point that we need go down and add them to current sum.

After every calculation in backtrack we see max of current_sum (either left/ right/ node/ total tree), is
giving us the max sum.

Steps
--------
1) Do DFS until reach leaf nodes.
2) Return SUM from every node. SUM = max(node, node+leftsum, node+rightsum) 
3) Update the MAX_SO_FAR = (MAX_SO_FAR, node, node+leftsum+rightsum, node+leftsum, node+rightsum)
4) Return MAX_SO_FAR, once DFS completed and get back to root.

Edge Cases
------------
1) When we see null node, return 0 as SUM, don't update MAX_SO_FAR.

Time Complexity: O(N)
Space Complexity: O(1)
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        MAX_SO_FAR = [-float("inf")]
        def dfs(node: TreeNode):
            if not node:
                return 0
            leftsum = dfs(node.left)
            rightsum = dfs(node.right)
            currentSum = max(node.val, node.val + leftsum, node.val + rightsum)
            MAX_SO_FAR[0] = max(MAX_SO_FAR[0], node.val+leftsum+rightsum, currentSum)
            return currentSum

        dfs(root)
        return MAX_SO_FAR[0] if MAX_SO_FAR[0] != -float("inf") else 0

# Testing
sol = Solution()
root = TreeNode(-10)
root.right = TreeNode(20)
root.left = TreeNode(9)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.maxPathSum(root))

root1 = TreeNode(11)
root1.right = TreeNode(20)
root1.left = TreeNode(9)
root1.right.left = TreeNode(5)
root1.right.right = TreeNode(7)
root1.right.left.right = TreeNode(5)
root1.right.left.left = TreeNode(-10)
print(sol.maxPathSum(root1))