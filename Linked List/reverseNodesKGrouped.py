"""
Reverse Nodes in k-Group

Difficulty: Hard

https://leetcode.com/problems/reverse-linked-list

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Solution (Brute Force)
----------
Convert linked list to multiple chunks array of size K, traverse from last chunk array in reverse and and reconstruct the linked list.

Time = O(N) Space = O(N)

Steps
-------
- Construct chunks of arrays from the linked list
- Traverse from right (end) to left (start) of the array and reconstruct the linked list

Solution (Optimised) - Iterative Approach
----------
Checking possibility of reversing K nodes in the linked list and reversing them in place.

Intuition
----------
Iterate throught the linked list while maintaining three pointers: previous, current, and next.
Possibly subfunctions
    - to find next K nodes if exist ot not
    - could reverse the each K group, where we keep nodes_count reversed and return group_head

Steps
-------
- First check whether next K nodes are existing to reverse, and return the Kth node if exist
- As we traverse the list, we keep a note on next pointer of current 
- Reverse the current's next to previous and then assign current node as next and new previous as current node
- Continue until current becomes null
- Finally the previous pointer will be at the new head of the reversed group list and return as group head
- On each iteration end append previous_group_head next as current_group_head


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:

    def checkNextKSizeNodes(self, k: int, node: ListNode):
        while node and k > 1:
            k -= 1
            node = node.next
        return node

    def getReversedListOfAGroup(self, next_to_last: ListNode, head: ListNode):
        prev = None
        current = head

        while current and current != next_to_last:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def reverseByKNodes(self, k: int, head: ListNode):
        dummyNode = ListNode(0)
        prev_group_tail = dummyNode
        current_head = head
        
        while True:
            last_node = self.checkNextKSizeNodes(k, current_head)
            if not last_node:
                break
            next_to_last = last_node.next
            current_group_head = self.getReversedListOfAGroup(next_to_last, current_head)
            if prev_group_tail:
                prev_group_tail.next = current_group_head
            prev_group_tail = current_head #as current first head node will be last after reversing
            current_head = next_to_last
        # either current_head will be a non reversed list group less than count K or current_head is None
        prev_group_tail.next = current_head
        
        return dummyNode.next

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reverse_list = sol.reverseByKNodes(6, head)

while (reverse_list):
    print(reverse_list.value, end="->")
    reverse_list = reverse_list.next