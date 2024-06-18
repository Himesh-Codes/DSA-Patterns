"""
Min Cost to Connect All Points
Difficulty: Medium
https://leetcode.com/problems/min-cost-to-connect-all-points/description/

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

https://www.youtube.com/watch?v=f7JOBJIC-NA&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=20

Solution (Prim's Algorithm)
-----------------------------
Minimum Spanning tree problem, considering each coordinate as a node and undirected graph have one node connected with all other nodes possibility (n2).
Similar to Dijkstra's algo, using the min-heap.

1) Find all the edges with adjancency matrix.
2) Keep a visited array to track visited item, and a min-heap (priority queue) for add items during BFS.
3) Min-heap used for find the minimum edge from current node to adjacent node and connect them toghether.
4) Stops the loop until the all nodes are connected, by checking visited nodes count is equal to total nodes.

Steps
------
1) Prepare adjacency list, with all edges, here all the nodes connected to other nodes (n2). Since that is the max possibility.
for i = 0... n and for j = i+1 ... n, since we add the distance from predeccessor nodes in previous traversal itself for both.
eg: i=1, j=3, we add adj[1] = [dist(1,3), 3] and adj[3] = [dist(1,3), 1] 
2) Rest step similar to Dijkstra's, extra cost variable to add the costs.
3) Add the cost(distance) and point as the value set in min-heap. Start with node 0, ie point[0] gives us a x,y coordinate, and distance as 0, since it is start node.
4) While heap not empty pop the element in min-heap, get min value.
5) If not visited then, add to total cost, add to visit
6) After this do a BFS on current node with adj list and push to min heap.
7) Do until visit node is equal to total number of nodes.

Time Complexity: O(n2logn), the min heap can have n2 values as max.
"""

import collections
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        n = len(points)

        for indexI in range(n):
            xI, yI = points[indexI]
            for indexJ in range(indexI+1, n):
                xJ, yJ = points[indexJ]
                distance = abs(xI - xJ) + abs(yI-yJ)
                adj_list[indexI].append([distance, indexJ]) #[cost, point]
                adj_list[indexJ].append([distance, indexI]) #[cost, point]

        cost = 0
        visited = []
        min_heap = [[0,0]]

        while min_heap and (len(visited) < n):
            dist, pointIndex = heapq.heappop(min_heap)
            if pointIndex in visited:
                continue
            visited.append(pointIndex)
            cost += dist

            # BFS of adj list
            for adjDistance, adjIndex in adj_list[pointIndex]:
                if adjIndex not in visited:
                    heapq.heappush(min_heap, [adjDistance, adjIndex])
        
        return cost

# Testing
sol = Solution()
print(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))