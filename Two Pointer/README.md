# Two Pointer

- Two pointers traverse the data structure together until a
  specific condition is met.
  - Handy for finding pairs in sorted arrays or linked lists, such
    as comparing elements to each other in an array.
  - Can be of different types - both pointers starting from
    same end, or one pointer at each end.

## Here are some common use cases of the two-pointer technique in Data Structures and Algorithms (DSA):

1. Finding Pairs in Sorted Arrays:

Two Sum: Given a sorted array and a target sum, find two elements that add up to the target.
3Sum: Find three elements that add up to a given target.
4Sum: Find four elements that add up to a given target.
Pair with Target Difference: Find two elements whose difference equals a given target.

2. Finding Subarrays with Specific Properties:

Maximum Subarray Sum: Find the contiguous subarray with the largest sum.
Minimum Size Subarray Sum: Find the smallest subarray with a sum greater than or equal to a given target.

3. Palindrome Checking:

Check if a string or linked list is a palindrome using two pointers, one moving forward and the other backward.

4. Linked List Operations:

Finding the Middle Node: Find the middle node of a singly linked list.
Reversing a Linked List: Reverse a linked list in-place using two pointers.
Removing Duplicates from a Sorted Linked List: Remove duplicates from a sorted linked list.

5. String Processing:

Valid Palindrome: Check if a string is a valid palindrome, considering only alphanumeric characters and ignoring cases.
Reverse Vowels of a String: Reverse only the vowels in a string.
Minimum Window Substring: Find the minimum-length substring containing all characters of a target string.

## Advantages of Using Two Pointers:

Reduced Time Complexity: Often leads to more efficient algorithms, reducing time complexity from O(n^2) to O(n) in many cases.
Constant Space Complexity: Typically requires only a constant amount of extra space, independent of the input size.
Simpler Implementation: Often results in more concise and readable code compared to alternative approaches.
