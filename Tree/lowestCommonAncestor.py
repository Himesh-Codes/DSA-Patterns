"""
 Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

 Difficulty: Medium
 Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q
 as descendants (where we allow a node to be a descendant of itself).”

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5

Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

Solution 
--------
We visit each and every node in tree with a DFS.

Steps
-------
1) Do a recursion on left and right nodes.
2) If node found return value, else return null.
3) So we can compare the left and right tree value, with recursive return value.
4) If both value is found in different branch of a parent then parent is the return value.
5) At the end either a common parent, or either the node itself might be parent of other node eg: 5 -right-> 4
Then the logic should return the 5, so catch here is if we found a number already we will return that.

Edge Case
----------
1) If the node is null, return null.
2) If node is either any of node value return that.
3) If the nodes are on the same path, since we return the first found element already it will be the LCA.
4) If left recursion is null, then return right.
5) If right recursion null, return left.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
            if root == None or root == p or root == q:
                return root
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if not right:
                return left
            elif not left:
                return right
            else:
                return root
            
        return dfs(root, p, q).val
        
        



# Testing
sol = Solution()
node = TreeNode(3)
node.left = TreeNode(5)
node.right = TreeNode(1)
node.left.left = TreeNode(6)
node.left.right = TreeNode(2)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)
node.left.right.left = TreeNode(7)
node.left.right.right = TreeNode(4)
print(sol.lowestCommonAncestor(node, 5, 1))