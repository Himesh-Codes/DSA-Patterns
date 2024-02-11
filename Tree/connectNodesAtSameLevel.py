"""
Connect Nodes at Same Level 
https://www.codingninjas.com/studio/problems/connect-nodes-at-same-level_985347

OR
Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

Complexity: Medium 

You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), 
your function should populate each next pointer to point to its next right node, 
just like in Figure B. The serialized output is in level order as connected by the next pointers, 
with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []
 
Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

Solution 1 (time : O(N), space: O(N))
-----------
BFS using level order traversal.

Steps
-------
1) Adding the each nodes in a queue. Like node.left and node.right which be push into queue.
2) And traverse and pop from queue FIFO, and last element in queue will have a NULL value for node.next.
3) Return the root node. 

Solution 2 (time : O(N), space: O(1)) Optimsed
-----------
We can mimic the same BFS without queue using two pointers current and nextchild node. 
And next iteration current will be swapped with next child (left), and nextchild will be 
nextchild.left (leftmost child), and so on.
Since current node will be already connected with it's right node in previous traversal, we can do current.next
And do connect it's left and right child.

Steps
-------
1) Assign root.next is None
2) Do a DFS with two pointers current and nextChild (current.left)
3) Connect current.left to current.right, with next pointer.
4) Then do BFS for connect right subtree childs at same level, call a function findRightConnectBFS,
that will traverse to current.next.
5) Repeat step 3 and do recursion of step 4 until current.next == None.
6) After this code run pointer come to DFS, do current = next, next = next.left.
7) Until current == None, do the recursion.

Edge cases
-------
1) If not root return root (None).
2) If root.left and root.right is not return root.

"""

"""
# Definition for a Node
"""
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or (not root.left and not root.right):
            return root
        root.left.next = root.right
        root.right.next = None

        def dfs(current):
            if not current.left and not current.right:
                return root
            
            current.left.next = current.right
            self.findRightConnnectBFS(current.next, current.right)
            return dfs(current.left)
        
        return dfs(root.left)
            
    def findRightConnnectBFS(self, current, lastRight):
        if not current:
                lastRight.next = None
                return
        lastRight.next = current.left
        current.left.next = current.right
        return self.findRightConnnectBFS(current.next, current.right)
        

# Testing
sol = Solution()
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)
root = sol.connect(node)
print(root.val)
def inorder(root):
    if root:
        inorder(root.left)
        print(f'value: {root.val}')
        if root.next: print(f'next value: {root.next.val}')
        inorder(root.right)
inorder(root)