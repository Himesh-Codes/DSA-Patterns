"""
Network Delay Time
Difficulty: Medium
https://leetcode.com/problems/network-delay-time/description/

You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, 
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

Solution (DijkStra's Algorithm)
---------------------------------
DijkStra's Algorithm: Minimum path algorithm with less time complexity O(ElogV) as compared to BellmanFord Algo.
Algorithm do BFS of all nodes with a min-heap to find the smallest edge among the heap.

Steps
-------
1) Get all the adjancency list of nodes; edges =  (u): [(v, w)], u is source node, v & w are  value and weight of destination node.
2) Use the priority queue/ min heap to add the node and distance. Keep a visited node array.
3) Start by adding the source and distance into queue [(0, K)].
4) Pop the queue until it is empty, when the item is poped in queue, do BFS, add the elements in it's adjacency list, mark the node as visited.
5) Add the elements into queue like (w1 + w2, node), weight of poped node (w1) and current adjacent element (w2).
6) Once poping the element take the new weight (here time is the wieght), update as min time needed.

Edge Cases
-----------
1) When ever visited array is size of all node (n), that is all node visited we can skip rest of the queue iteration.
Reduce and optimise the linear time complexity.
2) Return -1 if all nodes are not visited, else return min_time.

Time Complexity: O(ElogV)
"""
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # this is to delcare dynamic dictionary or hashmap
        adj_edges = collections.defaultdict(list)
        visited = []
        min_time = 0
        priority_queue = [(0, k)] #initialised with starting node

        for source, dest, time in times:
            adj_edges[source].append((dest, time))

        while priority_queue and (len(visited) < n):
            source_time , source = heapq.heappop(priority_queue)
            if source in visited:
                continue
            min_time = max(min_time, source_time)
            visited.append(source)

            for dest, time in adj_edges[source]:
                heapq.heappush(priority_queue, (source_time + time, dest))

        return min_time if len(visited) == n else -1

# Testing
sol = Solution()
print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))