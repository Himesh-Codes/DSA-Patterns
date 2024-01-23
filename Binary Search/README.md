# Binary Search

Technique used to traverse a decision tree or a sorted array. Efficiently find a specific element or the position to insert a new element in a sorted array.
Complexity of time is O(nlogn).

The binary search pattern technique is a powerful algorithmic approach in competitive programming that is particularly useful in scenarios where you need to efficiently search, find, or optimize over a monotonic sequence. Here are some situations where the binary search pattern is commonly applied:

- Searching in a Sorted Array:

Binary search is frequently used to find the index of a specific element in a sorted array. It has a time complexity of O(log n), making it more efficient than linear search for large datasets.

- Finding the Smallest or Largest Value:

If you need to find the smallest or largest value that satisfies a certain condition in a sorted sequence, binary search can be applied.

- Checking Feasibility:

Binary search can be used to check the feasibility of a solution in optimization problems. It helps determine the maximum or minimum value for which a certain condition holds true.

- Finding Peak Element:

Binary search is applicable to finding a peak element in an array. A peak element is an element that is greater than or equal to its neighbors.

- Finding Rotation Point in Rotated Sorted Array:

In cases where an array is rotated but still sorted, binary search can be used to find the rotation point or pivot element.

- Counting Occurrences:

Binary search can be applied to count the number of occurrences of a specific value in a sorted array.

- Square Root Calculation:

Binary search can be used to calculate the square root of a number with a specified precision.

- Minimization or Maximization:

In optimization problems, binary search can be used to minimize or maximize a certain function or objective.

- Searching in a 2D Matrix:

Binary search can be adapted to search for a specific element in a sorted 2D matrix.

- Interval or Range Search:

Binary search can be applied to find the position or range of values satisfying a certain condition within an interval.

Remember that for binary search to be applicable, the sequence must be monotonic, either in increasing or decreasing order. Additionally, binary search is most effective when the input space can be narrowed down by discarding half of it in each step.

It's crucial to understand the problem constraints, define the search space, and carefully implement the binary search pattern to handle edge cases and avoid errors. Practice and familiarity with the technique will improve your ability to apply it effectively in competitive programming.

General Indicators:

- Sorted Data: The problem involves a sorted array or list.
- Searchable Condition: The problem can be framed as searching for a value or boundary that satisfies a certain condition.
- Bounded Search Space: The possible solutions lie within a known range.
- Divide-and-Conquer Approach: The problem can be divided into smaller subproblems with similar structures.
- Logarithmic Time Complexity: The goal is to achieve an efficient solution with O(log n) time complexity.
