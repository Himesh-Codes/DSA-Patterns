# Linked List

In data structures and algorithms, linked lists are a fundamental concept. They consist of nodes where each node contains data and a reference (or link) to the next node in the sequence.
Linked lists come in different variations, and there are several patterns and techniques associated with them.
Here are some common patterns related to linked lists in the context of data structures and algorithms:

- Two Pointers (Slow and Fast Pointers):

Use two pointers to traverse the linked list at different speeds.
Commonly used for detecting cycles, finding the middle, or solving problems that involve pairs of nodes.

- Runner Technique:

Similar to the two pointers approach, involves iterating through the linked list with two pointers (runners).
Useful for detecting cycles, finding the middle, or solving problems that involve pairs of nodes.

- Recursive Reversal:

Reversing a linked list using recursion.
Break the problem down into smaller subproblems, reversing each part recursively.

- Dummy Nodes:

Introduce dummy nodes to simplify edge cases in insertion and deletion operations.
Helps avoid special handling for the head of the list.

- Merge Sort for Linked Lists:

Applying the merge sort algorithm to sort a linked list.
Divide the list into halves, sort each half, and then merge them back together.

- Cycle Detection (Floyd's Algorithm):

Use slow and fast pointers to detect cycles in a linked list.
Also known as the "tortoise and hare" algorithm.

- Intersection of Two Linked Lists:

Find the point of intersection of two linked lists.
Utilize pointers to adjust for the difference in length between the two lists.

- Flattening a Multilevel Doubly Linked List:

Handle linked lists that have multiple levels or layers.
Flatten the list to a single-level doubly linked list.

- Hashing for Duplicate Detection:

Use a hash table to keep track of visited nodes for duplicate detection.
Useful for problems where you need to identify and remove duplicates.

- Skip Pointers (Skip List):

Create multiple layers of linked lists with varying skip lengths.
Enables quick search, insertion, and deletion operations.

- Zigzag Traversal:

Traverse a linked list in a zigzag pattern (alternating directions).
Useful for problems where zigzag order is relevant.

- Reverse k-Group:

Reverse nodes in k-group chunks in the linked list.
Useful for problems that involve reversing segments of the list.
