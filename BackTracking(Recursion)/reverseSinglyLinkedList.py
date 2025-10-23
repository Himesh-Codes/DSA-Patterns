"""
Reverse Singly Linked List

Description: Given a singly linked list, reverse it using both iterative and recursive approaches, 
taking care of null and single-node lists. 

Test Cases :
Input: 1 → 2 → 3 → 4 → 5

Output: 5 → 4 → 3 → 2 → 1


Edge Input: null

Output: null


Edge Input: 42

Output: 42

Solution (Brute Force)
----------
Convert linked list to array, reverse the array and reconstruct the linked list.

Time = O(N) Space = O(N)

Steps
-------
- Construct an array from the linked list
- Traverse from right (end) to left (start) of the array and reconstruct the linked list

Solution (Optimised) - Iterative Approach
----------
Iterate through the linked list and reverse the pointers in place.
Time = O(N) Space = O(1)

Intuition
----------
Iterate throught the linked list while maintaining three pointers: previous, current, and next.

Steps
-------
- As we traverse the list, we keep a note on next pointer of current 
- Reverse the current's next to previous and then assign current node as next and new previous as current node
- Continue until current becomes null
- Finally the previous pointer will be at the new head of the reversed list

Solution (Optimised) - Recursive Approach (Backtracking)
----------
We can reverse the linked list recursively by reversing the rest of the list and then adjusting the pointers.
Time = O(N) Space = O(N) due to recursion stack

Intuition
----------
We recursively call the fuction until reach the end of the list.
While backtracking, we reverse the pointers.

Steps
-------
- Base case: if head is null or only one node, return head
- Recursively call reverse on head.next
- Keep track of new_head from recursion
- While backtracking , set head's next node's next as head and head's next to null
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Solution:
    new_head = None

    def recursion(self, head: ListNode):
        if not head.next:
            self.new_head = head
            return head
        
        self.recursion(head.next)
        head.next.next = head
        head.next = None

    def getReverseLinkedList(self, head: ListNode):
        self.recursion(head)
        return self.new_head

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reverse_list = sol.getReverseLinkedList(head)

while (reverse_list):
    print(reverse_list.value, end="->")
    reverse_list = reverse_list.next