"""
Remove Nth Node From End of List
Difficulty: Medium

https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Solution
----------
Traverse through entire singly linked list, keep a count on it's length. And then substract nth node number from length, to get the result node position. Iterate again with that result node position.
Using this technique we avoid the extra memory and complexity also reduced.

Eg: Input: head = [1,2,3,4,5], n = 2
Here we need to remove 4 that is 2 position from last. We can get len of linked list is 5, so resultant node position will be 5-2 + 1, since it is from last position.

Complexity: O(N)

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLength = 1
        node = head

        while node.next != None:
            node = node.next
            listLength += 1

        targetPreNodePosition = listLength - n
        node = head
        
        while targetPreNodePosition > 1:
            node =  node.next
            targetPreNodePosition -= 1
        if targetPreNodePosition == 0:
            head = node.next
        elif node.next != None: 
            node.next = node.next.next
        else: 
            return None

        return head 
    
# testing
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
print(sol.removeNthFromEnd(head, 2).val)