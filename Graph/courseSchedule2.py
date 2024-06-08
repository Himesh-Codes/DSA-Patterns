"""
Course Schedule II
Difficulty: Medium
https://leetcode.com/problems/course-schedule-ii/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, 
return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. 
So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. 
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

Topological Sort
----------
Topological Sort: Intuition is once a DFS is completed for a node it will visit and see the sub graphs and it's order.
DFS approach in a directed acyclic graph (DAG), since the undirected graph are not having a direction to sort.
ie 1 ---- 2, means it can be 1 ----> 2 or  1 <---- 2, means 1 before 2 and 2 before 1, so without direction we can't sort.
It is an algorithm based on adjacency list and doing DFS on each nodes with adjacency list.
With a visited trace, and do DFS only on non visited nodes.
LIFO stack to have the store the order of call in DFS.
AdjacencyList + DFS + Visited Array + Stack

Steps
--------
1) Create the adjacency matrix of each node
2) If the node is not visited do a DFS.
2) Do a DFS in each node adjacency matrix and DFS into the other nodes presented in adjacency matrix, 
until we see an empty adjacency list or already traversed node.
3) Make every node visited immediately once it is traversed.
4) When the DFS is completed for a node while track back in DFS add each node into stack.
5) At last when all node completed DFS, we have a stack filled with order in reverse order (LIFO).

eg:
4 ---> 0 <------ 5 -------> 6
|                |          |
|                |          |
v                v          |
2                3 <---------

Here, AdjMatrix = {0: [], 2: [], 3: [], 4: [0,2], 5:[0,3,6], 6:[3]}
From 0, no adj matrix so, added in stack = [0], and made visited
2, no adj matrix so, added in stack = [2,0], and made visited
3, no adj matrix so, added in stack = [3,2,0], and made visited
For 4, 0 & 2 already visited so no DFS,  added in stack = [4,3,2,0], and made visited
For 5, 3 visited, but 6 not visited dfs(6), given 3 in dfs of 6 is visited, so not adding 3 again
traverse back in DFS add 6 in stack = [6,4,3,2,0], now came back to DFS of 5 then do add to stack = [5,6,4,3,2,0] 

Trick To Find Cycle In DAG
----------------------------
While doing Topological Sort, we can keep a trace of DFS using a hashset, and detect a cycle, if a cycle comes it can't be sorted.
eg: 1---->2
    ^     |
    |     |
    3 <-----
Here 1 is before 2 in order, 2 before 3 inorder, 3 before 1 in order, since the parent 2 should after 1.

Time Complexity: O(E+V)
Space Complexity: O(N)

Solution 
---------
Using Topological Sort

Steps
-------
- Build adjacency matrix, that is the prerequisites of each node.
- Do a loop run in each nodes on adj matrix, and do DFS of each node, check condition where the dfs return false,
If False return empty array.
- Which inturn do a DFS on the adjacent matrix node of corresponding node.
- DFS should check in cycle if yes return False, if visited return True
- Check previous DFS is False while iterating through the prereq nodes or sub graphs. If False
return False
- If conditions not satisfied above, Keep a visited array appended.
- We use a trace with hashset to keep track of DFS and see a cycle is there, add to hashset.
- Add to the order stack while traverse back on DFS. Remove from cycle since the element already completed DFS.
- Return that order.

Edge Cases
-----------
1) If cycle is there return immediately an empty array (use a trace with hashset)
2) If the prerequisites/adj-list empty or adj-list nodes are already visited stop DFS.

Time Complexity: O(E+V)
Space Complexity: O(N)
"""
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adjmatrix = {course:[] for course in range(numCourses)}
        visited = []
        dfsTrace = []

        for course, preReqCourse in prerequisites:
            adjmatrix[course].append(preReqCourse)

        def dfs(course, prereq):
            # cycle check
            if course in dfsTrace: 
                return False
             # visited check 
            if course in visited: 
                return True
            
            visited.append(course)
            dfsTrace.append(course)

            # if adj list is empty / all adj nodes visited it stop DFS and add the current course to order
            for node in prereq:
                    if not dfs(node, adjmatrix[node]):
                        return False
            # once DFS completed and traceback remove course from the loop, since it doesnot contains in loop anymore
            dfsTrace.remove(course)
            order.append(course)
            return True

        for course in adjmatrix:
            dfsTrace = []
            if not dfs(course, adjmatrix[course]):
                return []

        return order

# Testing
sol = Solution()
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(sol.findOrder(2, [[1,0]]))
print(sol.findOrder(1, []))
print(sol.findOrder(2, [[1,0],[0,1]]))
print(sol.findOrder(3, [[0,1],[0,2],[1,2]]))