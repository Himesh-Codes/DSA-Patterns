"""
Connecting Cities With Minimum Cost
Difficulty: Medium
https://www.lintcode.com/problem/3672/

Description
There are n cities in this question, and their numbers range from 1 to n.

At the same time, there is a connections array and connections[i]= [ai, bi, ci], which means that the cost of connecting cities 
ai and bi is ci.

Please return the minimum cost required to connect all cities. If all cities cannot be connected, return -1.

Example 1

Input:

3
[[1,2,1], [2,3,2], [1,3,3]]
Ouput:

3

Explanation:

Choose [1,2,1] and [2,3,2] to connect all n cities. At this time, the cost is the least, which is 3.

Example 2

Input:

3
[[1,2,1]]
Output:

-1

Explanation:

Unable to connect all cities according to connections

Solution
----------
Kruskal Algorithm : Combination of Union Find + Min Heap/ Priority Queue

Steps
-------
- Sort all the edges in ascending order (we can use min heap, the priority queue here)
- Use union find algorithm, for getting MST
- Considering each node is parent of itself.

Edge Cases
-------------
- Either return total cost calculated during MST creation 
- Or if number of visited nodes is less than total number of cities, return -1.

Time Complexity: O(E+V)
Space complexity: O(E+V)
"""
from typing import (
    List,
)
import heapq

class Solution:
    """
    @param n: the number of cities
    @param connections: the connection info between cities
    @return: 
    """
    def minimum_cost(self, n: int, connections: List[List[int]]) -> int:
        totalcost = 0
        priorityQueue = []
        parent = [index for index in range(1, n+1)]
        rank = [1] * n
        # use set to ignore duplicate entry
        mergedNodes = set()

        for source, destination, cost in connections:
            heapq.heappush(priorityQueue, [cost, source, destination])
        
        def findParent(node):
            while node != parent[node-1]:
                parent[node-1] = parent[parent[node-1]]
                node = parent[node-1]
            return node

        def unionNodes(nodeOne, nodeTwo):
            parentOne, parentTwo = findParent(nodeOne), findParent(nodeTwo)
            
            # edge cases if root parents are same already added to the component
            if parentOne == parentTwo:
                return 0
            
            # accessing index is index-1 since the number starts from 1...n
            if rank[parentOne-1] > rank[parentTwo-1]:
                parent[parentTwo-1] = parentOne
                rank[parentOne-1] += rank[parentTwo-1]
            else:
                parent[parentOne-1] = parentTwo
                rank[parentTwo-1] += rank[parentOne-1]
            return 1

        while priorityQueue:
            cost, source, destination = heapq.heappop(priorityQueue)
            join = unionNodes(source, destination)
            if join:
                totalcost += cost
                mergedNodes.add(source)
                mergedNodes.add(destination)
        
        return totalcost if len(mergedNodes) == n else -1
    

# Testing
sol = Solution()
print(sol.minimum_cost(3, [[1,3,3], [1,2,1], [2,3,2]]))
print(sol.minimum_cost(3, [[1,2,1]]))