# Dynamic Programming

Dynamic programming is a method used in computer science to solve optimization problems by breaking them down into simpler subproblems and storing the solutions to those subproblems to avoid redundant calculations. It's particularly useful when the problem can be divided into overlapping subproblems, allowing for re-use of solutions.

## Thought Process

Find the bruteforce solution for a problem and see how we can do create and memoize the subproblems.
That will help the suceeding/preceeding subproblem to help it's calculation based on output from
suceeding/preceeding DP, respectively for top to bottom / bottom to top approach.

In the context of data structures and algorithms, dynamic programming often comes into play when solving problems like:

- Fibonacci sequence: Calculating Fibonacci numbers can be optimized using dynamic programming to avoid redundant recursive calls.

- Shortest path problems: Algorithms like Dijkstra's or Floyd-Warshall's can utilize dynamic programming to efficiently find the shortest path between nodes in a graph.

- Knapsack problem: Dynamic programming can be used to efficiently solve the 0-1 knapsack problem, where you have to select a subset of items to maximize the total value without exceeding a given weight capacity.

- Longest common subsequence: Dynamic programming can be applied to find the longest subsequence common to two sequences, which is a fundamental problem in bioinformatics, text analysis, and version control systems.

- Matrix chain multiplication: Given a sequence of matrices, dynamic programming can be used to find the most efficient way to multiply them together.

In all these cases, dynamic programming helps avoid redundant calculations by storing and reusing intermediate results, leading to significant improvements in time and space complexity compared to naive approaches.

References:

- How to approach DP: https://www.linkedin.com/feed/update/urn:li:activity:7218822388912676864/
- Common DP patterns https://www.youtube.com/watch?v=mBNrRy2_hVs&t=36s
- DP patterns sheet - https://docs.google.com/spreadsheets/d/14VDA1KjrHQ_B3Zz763J4KCcK0l0r3AE6wS085Xp08bU/edit?gid=0#gid=0
