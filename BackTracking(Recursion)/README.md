# Backtracking

If the problem asks for subsets / permutations, we use the backtracking mostly.

Backtracking is a general algorithmic technique that incrementally builds candidates to solutions and abandons a candidate as soon as it determines that the candidate cannot possibly lead to a valid solution. This approach is often used in scenarios involving constraint satisfaction problems. Here are some key uses and examples of backtracking in the context of data structures and algorithms:

- Combinatorial Problems:

  Permutations: Generating all permutations of a set of elements. For example, finding all possible arrangements of a set of numbers.

  Combinations: Generating all combinations of a set of elements. For example, choosing k elements from a set of n elements.

- Puzzle Solving:

  Sudoku: Filling a 9x9 grid so that each row, column, and 3x3 subgrid contains all digits from 1 to 9. Backtracking tries numbers sequentially and backtracks if a conflict arises.

  N-Queens Problem: Placing N queens on an N×N chessboard such that no two queens threaten each other. Backtracking places queens one by one and checks for conflicts.

- Graph Problems:

  Hamiltonian Path and Cycle: Finding a path or cycle in a graph that visits each vertex exactly once. Backtracking explores each path and abandons it if it revisits a vertex.

  Coloring Problem: Assigning colors to the vertices of a graph such that no two adjacent vertices share the same color. Backtracking tries different colors and backtracks if a conflict arises.

- Constraint Satisfaction Problems (CSPs):

  Crossword Puzzle: Placing words in a crossword grid such that they fit both the horizontal and vertical constraints.

  Map Coloring: Coloring a map with a limited number of colors such that no adjacent regions share the same color.

- String Problems:

  Regular Expression Matching: Matching strings against complex patterns. Backtracking explores different ways of matching parts of the pattern with parts of the string.

  Word Search: Finding a sequence of letters in a grid to form a word. Backtracking explores different paths in the grid to form the word.

- Optimization Problems:

  Knapsack Problem: Finding the optimal subset of items to include in a knapsack without exceeding its capacity. Backtracking explores different subsets and backtracks if the capacity is exceeded.

- Subsets and Subsequences:

  Generating Subsets: Finding all subsets of a given set. Backtracking explores the inclusion and exclusion of each element.

  Longest Increasing Subsequence: Finding the longest subsequence of a sequence where the elements are in increasing order. Backtracking explores different subsequences and backtracks if the order is violated.

Backtracking Patterns: https://lnkd.in/g9csxVa4
Backtracking Patterns 2: https://lnkd.in/gVkQX5vA
