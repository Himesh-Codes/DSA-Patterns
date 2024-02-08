"""
Insertion Sort List
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. 
One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 
Complexity: O(N2)

Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000

https://leetcode.com/problems/insertion-sort-list/description/

Solution
------------
The insertion sort check the one node and it's previous node compare if it is less than previous node.
Then it will traverse from head to previous node and insert in accurate position.
Thus the left side of list will be sorted always on traversal, from head to end.
 
Steps
-------
- For elimanate the head value based edge cases, we create a dummy node prepend to head.
- Traverse from head to end node.
- On traversal check the previous element is greater than current code. 
- If yes then continue traversal.
- Else traverse on left hand side sorted list dummy node head to previous element, or until condition current node value
is greater than sorted side list traversal pointer (sortedNode). And insert on a position where sortedNode.next value
is greater than current node.
- Do same until the list traversal completed
- And return dummy.next that is our actual head.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head and head.next == None:
            return head
        
        dummy = ListNode(0, head)
        previousNode, currentNode = head, head.next
        while currentNode:
            if currentNode.val >= previousNode.val:
                previousNode, currentNode = currentNode, currentNode.next
                # push the control to while loop starting
                continue

            # currentNode is less than previous node
            sortedNode = dummy
            # compare with sortedNode next value, 
            # so sorted node is previous node of lesser node than current node value
            while currentNode.val > sortedNode.next.val:
                sortedNode = sortedNode.next
            # once the position for insert in between sortedNode and sortedNode.next found
            previousNode.next = currentNode.next
            currentNode.next =  sortedNode.next
            sortedNode.next = currentNode
            # The previosnode.next will be our next current
            currentNode = previousNode.next

        return dummy.next

