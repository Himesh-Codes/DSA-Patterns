# Segment Tree

A Segment Tree is a powerful data structure that is used for storing information about intervals or segments. It allows querying and updating ranges of data efficiently. It is particularly useful for scenarios where there are frequent updates and queries of ranges, which would be inefficient with simpler data structures like arrays or linked lists.

## Structure and Operations

A Segment Tree is typically represented as a binary tree where each node represents an interval or segment of the array. The root node represents the entire array, and each leaf node represents a single element of the array.

## Construction

Building a Segment Tree from an array of size 𝑛 takes 𝑂(𝑛) time. Here’s a brief outline of the steps:

- Start with the leaves representing individual elements of the array.
- Each internal node of the tree represents the combination (e.g., sum, min, max) of its child nodes.
- The root node represents the combination of the entire array.

## Common Operations:

- Build the Tree: Construct the segment tree from an initial array.
- Range Query: Query for an aggregate function (like sum, minimum, maximum, greatest common divisor, etc.) over a range.
- Update: Update an element or a range of elements in the array.

## Applications

Segment Trees have several applications, particularly in scenarios requiring efficient range queries and updates. Below are some of the key applications:

1. Range Sum Queries
   Problem: Given an array, efficiently calculate the sum of elements between two given indices.
   Solution: Use a Segment Tree where each node stores the sum of a segment of the array.
2. Range Minimum/Maximum Queries
   Problem: Find the minimum or maximum value in a subarray.
   Solution: Use a Segment Tree where each node stores the minimum or maximum value in a segment.
3. Range GCD Queries
   Problem: Compute the greatest common divisor (GCD) of all numbers in a subarray.
   Solution: Use a Segment Tree where each node stores the GCD of a segment.
4. Interval Updates and Queries
   Problem: Efficiently update the values in a subarray and query the updated values.
   Solution: Use a Segment Tree that supports lazy propagation to handle range updates efficiently.
5. Counting Elements in a Range
   Problem: Count the number of elements within a specific range that satisfy a given condition.
   Solution: Use a Segment Tree where each node stores a count of elements satisfying the condition in a segment.
6. Dynamic Array
   Problem: Perform dynamic range queries and updates on an array where elements are frequently added or removed.
   Solution: Use a Segment Tree that supports dynamic operations.
