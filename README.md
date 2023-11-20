# DSA-Patterns

A pattern based DSA approaches exploration and study new techniques on the way.

## Pattern Based Roadmap

https://neetcode.io/roadmap

`Top Practice Question` - https://neetcode.io/practice

Other reference sources

- https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/
- https://www.geeksforgeeks.org/sde-sheet-a-complete-guide-for-sde-preparation/

## Most Use DSA Patterns

✅ Arrays

- Binary Search
- Sorting
- Two Pointers
- Sliding Window
- Prefix Sums
  ✅ Recursion (Decision Trees)
- Binary Trees
- Tries
- Backtracking
  ✅ Graphs
- Depth-first-search
- Breadth-first-search
  ✅ HashMaps
  ✅ Hea

## Identify Pattern To Use

`If given a linked list then`

✒ Two pointers

`If the input array is sorted then`

✒ Binary search

✒ Two pointers

`If asked for all permutations/subsets then`

✒ Backtracking

`If given a tree or a graph then`

✒ DFS

✒ BFS

`If recursion is banned then`

✒ Stack

`If must solve in-place then`

✒ Swap corresponding values

✒ Store one or more different values in the same pointer

`If asked for maximum/minimum subarray/subset/options then`

✒ Dynamic programming

`If asked for top/least K items then`

✒ Heap

`If asked for common strings then`

✒ Map

✒ Trie

`General Tips`

✒ Map/Set for O(1) time & O(n) space

✒ Sort input for O(nlogn) time and O(1) space

## DS based patterns elaborated

`Array and Strings:`

- Two Pointers:

Used for searching pairs in a sorted array, or when there are two constraints that can be managed simultaneously.

- Sliding Window:

Efficiently process arrays or lists by maintaining a subset of elements within a range.

- Prefix Sum:

Useful for finding the sum of elements in a subarray, especially when dealing with cumulative data.

- Binary Search:

Efficiently find a specific element or the position to insert a new element in a sorted array.

`Linked Lists`:

- Fast and Slow Pointers:

Detect cycles in linked lists or find the middle of the list.

- Reverse a Linked List:

Reverse the order of elements in a linked list.

`Trees and Graphs:`

- Depth-First Search (DFS):

Traverse or search through a tree or graph by going as deep as possible before backtracking.

- Breadth-First Search (BFS):

Traverse or search through a tree or graph level by level.

- Binary Tree Traversal:

Inorder, Preorder, and Postorder traversals for binary trees.

- Topological Sorting:

Order nodes in a directed acyclic graph (DAG) such that each node comes before all nodes to which it has outgoing edges.

`Dynamic Programming:`

- Memoization:

Store previously computed results to avoid redundant calculations in recursive algorithms.

- Tabulation:

Build a table and fill it incrementally, often used in bottom-up dynamic programming.

- Longest Common Subsequence (LCS):

Find the longest subsequence present in given sequences (can be strings, arrays, etc.).

- Knapsack Problem:

Solve optimization problems where the goal is to maximize or minimize a value subject to constraints.

`Greedy Algorithms:`

- Interval Scheduling:

Select a maximum-size set of non-overlapping intervals.

- Huffman Coding:

Efficiently encode characters based on their frequencies in a given text.

`Backtracking:`

- N-Queens Problem:

Place N queens on an N×N chessboard in such a way that no two queens threaten each other.

- Subset Generation:

Generate all possible subsets of a set.

## Patterns Usage Techniques Elaborated

- Two Pointers

  - Two pointers traverse the data structure together until a
    specific condition is met.
  - Handy for finding pairs in sorted arrays or linked lists, such
    as comparing elements to each other in an array.
  - Can be of different types - both pointers starting from
    same end, or one pointer at each end.

    `Psuedo Code Availbale In PDF "Patterns DSA"`

    Problems based on Two
    Pointers:

    - [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
    - Squares of a Sorted Array
    - 3Sum
    - 3Sum Closest
    - Sort Colors
    - Backspace String Compare

- Fast and Slow Pointers

  - Also known as the Hare & Tortoise algorithm uses two
    pointers which move through the data structure at
    different speeds

    Problems

    - Linked List Cycle
    - Happy Number
    - Palindrome Linked List
    - Reorder List
    - Circular Array Loop

- Sliding Window

  - Used to perform a required operation on a specific window
    size of a given array or linked lis

  - Useful for problems dealing with subarrays or sublists

    `Psuedo Code Availbale In PDF "Patterns DSA"`

    Problems

    - Maximum Average Subarray I
    - Minimum Size Subarray Sum
    - Longest Substring with At Most K Distinct Characters
    - Fruit Into Baskets
    - Longest Substring with At Most Two
      Distinct Characters
    - Longest Substring Without Repeating
      Characters
    - Max Consecutive Ones III
    - Minimum Window Substring
    - Find All Anagrams in a String

- Merged Intervals

  - This technique is used to deal with problems that require
    you to find overlapping intervals.

    Problems

    - Insert Interval
    - Interval List Intersections
    - Meeting Rooms
    - Meeting Rooms II
    - Car Pooling
    - Employee Free Time

- Depth First Search (DFS)

  - Recursive Algorithm used to search all the vertices of all a
    graph or a tree.
  - It starts from a chosen source node and explores as far as
    possible along each branch before backtracking

    `Psuedo Code Availbale In PDF "Patterns DSA"`

    Problem

    - Path Sum II
    - Binary Tree Paths
    - Sum Root to Leaf Numbers
    - Path Sum III
    - Diameter of Binary Tree
    - Binary Tree Maximum Path Sum

- Breadth First Search (BFS)

  - BFS is a graph traversal algorithm that systematically
    explores all the nodes in a graph by visiting nodes in layers
    or levels
  - Starts from a chosen source node, visits all its neighbors,
    then moves on to their neighbors, and so on, until all nodes
    are visited or a specific condition is met.$
  - Uses a queue data structure

    Problems

    - Binary Tree Level Order Traversal II
    - Binary Tree Zigzag Level Order Traversal
    - Average of Levels in Binary Tree
    - Maximum Level Sum of a Binary Tree
    - Minimum Depth of Binary Tree
    - Maximum Depth of Binary Tree
    - Populating Next Right Pointers in Each Node
    - Binary Tree Right Side View

## Pattern Articles

- Backtracking Patterns: https://lnkd.in/g9csxVa4

- Sliding Window patterns: https://lnkd.in/gjatQ5pK

- Sliding Windows on Strings Pattern: https://lnkd.in/gX8ebtnb

- Two Pointers Patterns: https://lnkd.in/gBfWgHYe

- Substring Problem Patterns: https://lnkd.in/gdGtE72g

- Tree Patterns: https://lnkd.in/gKja_D5H

- Tree Iterative Traversal: https://lnkd.in/gGpXjHt5

- Dynamic Programming Patterns: https://lnkd.in/gbpRU46g

- Binary Search Patterns: https://lnkd.in/gKEm_qUK

- Monotonic Stack Patterns: https://lnkd.in/gdYahWVN

- Bit Manipulation Patterns: https://lnkd.in/gkxVZTXU

- Graph Patterns: https://lnkd.in/gKE6w7Jb

- DFS + BFS Patterns (1): https://lnkd.in/gPgpsgaQ

- DFS + BFS Patterns (2): https://lnkd.in/gd4ekfQe

- 14 Coding Interview Patterns: https://lnkd.in/gMZJVkFf

## 10 Leetcode articles that will make your coding interview preparation lot easier and save you tons of time:

- Sliding Window patterns: https://lnkd.in/gjatQ5pK

- Two Pointers Patterns: https://lnkd.in/gBfWgHYe

- Substring Problem Patterns: https://lnkd.in/gdGtE72g

- Dynamic Programming Patterns: https://lnkd.in/gbpRU46g, https://lnkd.in/gcnBActT

- Binary Search Patterns: https://lnkd.in/gKEm_qUK

- Backtracking Patterns: https://lnkd.in/gVkQX5vA

- Tree Patterns: https://lnkd.in/gKja_D5H

- Graph Patterns: https://lnkd.in/gKE6w7Jb

- Monotonic Stack patterns: https://lnkd.in/gdYahWVN

## Competition Practices

- 𝐋𝐞𝐞𝐭𝐂𝐨𝐝𝐞: - They have Bi-Weekly(Saturday 8 PM) and Weekly(Sunday 8 AM) contests in which we have to do 4 questions in 90 min.
  You have to compete with the best minds around the world. Almost 20k+ users give the contest.
  ∙ 𝐋𝐢𝐧𝐤: https://lnkd.in/dzqNzcpp

- 𝐆𝐞𝐞𝐤𝐬𝐅𝐨𝐫𝐆𝐞𝐞𝐤𝐬: They have a Weekly Interview Series every Sunday at 7 PM in which you have to solve 3 questions in 90 min.
  They replicate coding interview rounds of many big companies. After the contest, they explained everything in a video editorial on YouTube too.
  ∙ 𝐋𝐢𝐧𝐤: http://bit.ly/3grLkLs

## Top 50 DSA Qns (By SDE Ashish Amazon)

Here are Top 50 of them:

1. Furthest Building You Can Reach: https://lnkd.in/gup4SjT3

2. Maximum Points You Can Obtain from Cards: https://lnkd.in/g46uuRRY

3. Trim a Binary Search Tree: https://lnkd.in/ggZjxhfB

4. Car Pooling: https://lnkd.in/gHYDuBB3

5. Two Sum: https://lnkd.in/gvmrSsPf

6. Container With Most Water: https://lnkd.in/g3wzbAdt

7. Distribute Coins in Binary Tree: https://lnkd.in/gB5jwdYP

8. Merge Two Sorted Lists: https://lnkd.in/gWiNc4iT

9. Merge k Sorted Lists: https://lnkd.in/gC7XdcYn

10. Group Anagrams: https://lnkd.in/g2ZvQCMt

11. Merge Intervals: https://lnkd.in/gj7mKaC7

12. Rotting Oranges: https://lnkd.in/gQPtGtBE

13. Diameter of Binary Tree: https://lnkd.in/gpgf_bxQ

14. Top K Frequent Elements: https://lnkd.in/gQ7YbpyG

15. Sliding Window Maximum: https://lnkd.in/gPxyzZte

16. Number of Islands: https://lnkd.in/g4SuhAKZ

17. Linked List Cycle II: https://lnkd.in/gvgpiPeb

18. Jump Game II: https://lnkd.in/gi2e6HwH

19. Maximum Subarray: https://lnkd.in/gvXACXww

20. Longest Increasing Path in a Matrix: https://lnkd.in/g832N7kP

21. Trapping Rain Water: https://lnkd.in/gyj3KRzF

22. Reverse Linked List: https://lnkd.in/gFdtXjpp

23. Course Schedule II: https://lnkd.in/g-zYyETQ

24. Sort Colors: https://lnkd.in/gkdR3wW8

25. Implement Trie (Prefix Tree): https://lnkd.in/gAH5a-7M

26. Move Zeroes: https://lnkd.in/g-zKby4V

27. Daily Temperatures: https://lnkd.in/gEDjGxz8

28. Insert Delete GetRandom O(1): https://lnkd.in/gCNhaage

29. Longest Increasing Subsequence: https://lnkd.in/gQa8vA23

30. Populate Next Right Pointers In Each Node II: https://lnkd.in/g_NM2kcb

31. Binary Tree Maximum Path Sum: https://lnkd.in/gsQNe33B

32. Longest Substring Without Repeating Characters: https://lnkd.in/gGUhV_Cm

33. Combination Sum: https://lnkd.in/gE3rVnJi

34. Unique Binary Search Trees II: https://lnkd.in/g8n6wZvP

35. First Bad Version: https://lnkd.in/gm4NqwNY

36. Word Search II: https://lnkd.in/geXH9tc3

37. Task Scheduler: https://lnkd.in/g2JF77Fs

38. Bus Routes: https://lnkd.in/gdXVMMVp

39. Reconstruct Itinerary: https://lnkd.in/ga2KSv4h

40. Maximum Profit in Job Scheduling: https://lnkd.in/gb_qP8vA

41. Cheapest Flights Within K Stops: https://lnkd.in/grHsBbR6

42. Stock Price Fluctuation: https://lnkd.in/g4yuZgQF

43. Subarray Sum Equals K: https://lnkd.in/gbxm_NXC

44. Delete Nodes And Return Forest: https://lnkd.in/g6Xx3uc7

45. Coin Change II: https://lnkd.in/gYhka_-y

46. Clone Graph: https://lnkd.in/gMqAMeSv

47. Rotate Image: https://lnkd.in/gBny5AMK

48. Convert Sorted Array to Binary Search Tree: https://lnkd.in/gT7tm5fJ

49. Process Tasks Using Servers: https://lnkd.in/gMYbjGWB

50. Min Stack: https://lnkd.in/gPCwDHiT

## FAANG TOP Interview Questions

- 4Sum II :- https://lnkd.in/dGwh5E6H

- Fizz Buzz :- https://lnkd.in/dyqP4sb6

- Longest Substring with At Least K Repeating Characters :- https://lnkd.in/dPcT3_mK

- First Unique Character in a String :- https://lnkd.in/d6Uqtw6i

- Shuffle an Array :- https://lnkd.in/dNZfRWdc

- Insert Delete GetRandom O(1) :- https://lnkd.in/dyna5k4m

- Kth Smallest Element in a Sorted Matrix :- https://lnkd.in/dAyEEsKg

- Sum of Two Integers :- https://lnkd.in/dkZvBefp

- Intersection of Two Arrays II :- https://lnkd.in/dXNkr2fK

- Top K Frequent Elements :- https://lnkd.in/d59AZZRm

- Reverse String :- https://lnkd.in/d8Vf2VW2

- Flatten Nested List Iterator :- https://lnkd.in/ddKVBXgr

- Increasing Triplet Subsequence :- https://lnkd.in/ddzyypTJ

- Longest Increasing Path in a Matrix :- https://lnkd.in/dBWX52A5

- Odd Even Linked List :- https://lnkd.in/dPuzPfJr

- Power of Three:- https://lnkd.in/dR8zcCKr

- Wiggle Sort II :- https://lnkd.in/dUMCb-5h

- Coin Change :- https://lnkd.in/dquhDTjZ

- Count of Smaller Numbers After Self :- https://lnkd.in/d69xU9By

- Longest Increasing Subsequence :- https://lnkd.in/dDjGzqVj

- Serialize and Deserialize Binary Tree :- https://lnkd.in/dmY5Ftxj

- Find Median from Data Stream :-https://lnkd.in/dE_n_6Uq

- Game of Life :- https://lnkd.in/dHRVuZbF

## Sample Interview Preparation Strategy

Here's the whole strategy divided into 3 parts:

1. Data Structures & Algorithms Preparation

Solving a lot of problems on Leetcode/GFG won't help unless you are solving "Quality" problems.
I focused more on solving problems that were of medium level and emphasized quality over quantity.
It will take atleast a 4-5 month consistent effort to get good in this section.

2. Projects

When deciding to build projects, you must make sure that you avoid copying them from your seniors or friends just for the sake of doing it.
During interviews, if the interviewer delves into the depths of the tech stack used in your project, you will face difficulties answering those questions.

I chose a project in which I had command over the tech stack and also prepared for possible questions that might arise based on it.
Attribute atleast 3-4 months to this section while solving 2-3 leetcode questions daily.

3. Core Subjects (DBMS/OS/CN)

You can refer to the Gate Smashers playlist on YouTube to study the concepts, and questions on GeeksforGeeks can really complement your preparation.

Last but not least, basic skills like communication also help during the interviews, so make sure you are able to explain the solution to the interviewer.
