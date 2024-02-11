"""
MergeSort Linked List
Difficulty: Medium

https://leetcode.com/problems/sort-list/description/
https://www.codingninjas.com/studio/problems/mergesort-linked-list_630514

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
Sort the list using the 'Merge Sort' algorithm.
Ref: https://www.youtube.com/watch?v=TGveA1oFhrc

Complexity: O(NlogN)

Solution
---------
Using merge sort give O(nlogn) solution, but memory is O(logN)
Divide and conquer approach with O(lognN) and merge the list of N size gives the O(N), for the merge sort 
in linked list.

Steps
-------
1) Get the middle element in linkedlist. Using fast and slow pointer concept, if slow is head (1st element)
 and fast is head.next(2nd element), 
slow pointer move in 1x speed and fast pointer in 2x speed.
Once fast pointer is Null, the slow pointer is in mid.
ie, 1 mid for list with size 2. 
2 is mid of size 3 & 4, 
3 is mid for size 5 & 6.
4 is mid for size 7 & 8.
So if fast pointer is in 2 * position of slow we can easily find one list mid.
On every iteration we check fast is not None and fast.next not None (this is for odd size cases like 5, 7)
2) To split the linkedlist into 2 equal element length, we find mid and
 make left - mid (make mid.next = None, so it is not more connected and splitted list), and mid.next - right.
3) Use recursion for the divide and conquer.
4) Merge the list after the each and every split you get from the divide and conquer is sorted.

Edge Cases
----------
1) If head is null then, return None.
2) If head is single element return head.

"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        mid = self.findMid(head)
        right = mid.next
        # decoupled the list and seperated now to right and left
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeList(left, right)

    def findMid(self, node: ListNode):
        slow, fast = node, node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def mergeList(self, left: ListNode, right: ListNode):
    
        tail = head = ListNode()
      
        while left and right:
            if left.val < right.val:
                tail.next = left 
                left = left.next
            else:
                tail.next = right  
                right = right.next
            
            tail = tail.next
        if left:
            tail.next = left 

        if right:
            tail.next = right 
        return head.next

# testing
sol = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

ex = [4,19,14,5,-3,1,8,5,11,15]

head = ListNode(4)
head.next = ListNode(19)
head.next.next = ListNode(14)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(-3)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next.next = ListNode(11)
head.next.next.next.next.next.next.next.next.next = ListNode(15)

res = sol.sortList(head)

while res:  
    print(res.val)
    res = res.next
