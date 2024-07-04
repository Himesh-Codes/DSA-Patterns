"""
Critical Connections in a Network
Difficulty: Hard
https://leetcode.com/problems/critical-connections-in-a-network/description/
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections 
forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi.
 Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some 
other server.

Return all critical connections in the network in any order.

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]


Bridges In A Graph / Find SCCs
------------------
If an edge is getting removed, it can create 2 single standalone interconnected component.

Eg: 2 ------- 1                 8 --------- 7
    |         |                 |           |
    |         |                 |           |
    3 ------- 4 ----- 5 ------- 6 -----------

    Here if we remove edge 4 --- 5 it split to 2 standalone component 1,2,4,3 and 5,6,7.
    But imagine if we remove 2 --- 1, it doesnot make any sense still no component fix
    1, 2, 3, 4, 5, 6, 7 are connected each other.

Bridges: The edges that connecting 2 SCC's are called bridges. If bridge is removed the two SCC's become
standalone components.
In the above example the bridges are 4 --- 5 and 5 ---- 6.

Solution (Tarjan's Algorithm)
------------------------------
Intuition is if there exist a route from current node to it's parent node, without it's connecting edge
we can say the edge removal will make the whole component splitted into 2 indivudual component.
So at the end the insertion time on start node of SCC will be the lowest time of it's adjacent components
in SCC.
https://www.youtube.com/watch?v=qrAub5z8FeA

1) DFS is the key. And keep the visited node array track to not to visit again.
2) While doing DFS we will keep 2 tracks.
3) insertion_time = [], Time of insertion, we can keep the value of time we visited the node. 
4) lowest_time = [], Lowest time of insertion among all it's adjacent nodes, but not from parent.
Once we visit an adjacent already visited and have lowest_time lower than it's lowest_time, 
we update the lowest_time[currentnode] = lowest_time[alreadyvisitedadjacent], but not from parent.

While backtrack we need to update lowest among the child and parent and update parent.
lowest_time[parent] = min(lowest_time[child], lowest_time[parent])

Eg: 2 ------- 1                 8 --------- 7
    |         |                 |           |
    |         |                 |           |
    3 ------- 4 ----- 5 ------- 6 -----------

After this DFS is completed all the connected components will have a same lowest time of insertion.
eg: Start DFS from node 1, node 1 will have insertion_time [1:1], and lowest_time [1:1], 
visited array have [1]
DFS next node 2, node 2 will have insertion_time [2:2], and lowest_time [2:2]
DFS next node 3, node 3 will have insertion_time [3:3], and lowest_time [3:3]
DFS next node 4, node 4 will have insertion_time [4:4], and lowest_time [4:4]
DFS next node 5, node 5 will have insertion_time [5:5], and lowest_time [5:5]
DFS next node 6, node 6 will have insertion_time [6:6], and lowest_time [6:6]
DFS next node 7, node 7 will have insertion_time [7:7], and lowest_time [7:7]
DFS next node 8, node 8 will have insertion_time [8:8], and lowest_time [8:8]
visited array have [1,2,3,4,5,6,7,8]

Now come the interesting point the node 8 have adjacent node 6 that is already visited.
That means if we think we remove edge 7 ---- 8, still 8 can visit 7 through  8 --> 6 --> 7.
So no point that we remove the edge, and it's not a bridge.

Now while we traverse node 6 from node 8 we see lowest of adjacent node 6 is lowest_time [6:6]
and it is lower than node 8 lowest_time [8:8], so we update lowest time of 8 as lowest_time [8:6]

Again we backtrack to node 7 from node 8, now lowest of it's child 8 is lower than node 7.
, so we update lowest time of 8 as lowest_time [7:6].

Again we go to node 5 on backtrack but node 5 is having lowest time than node 6.
We backtrack to node 4, still we need to visit the node 1 from node 4, that is not parent of node 4,
so we update lowest time of 4 as lowest_time [4:1].
While backtrack to 3 we update lowest time of 4 as lowest_time [3:1].
While backtrack to 2 we update lowest time of 4 as lowest_time [2:1].

Now lowest time are.
[1:1], [2:1], [3:1], [4:1], [5:5], [6:6], [7:6], [8:6]
All nodes have the same lowest time is an SCC.
So we know bridge is 4 -- 5 and 5 -- 6.

Steps
------
1) Create adj list since this is not directed graph, while building adj_list we take
adj[u] = [v] and adj[v] = [u]
Inititialise insert_time and low_time, Do the DFS
2) Update with time of visit when dfs on node, DFS on adjacent nodes also.
3) If adj node is the parent of node itself, it is not creating a bridge so skip it.
4)low_time is updated when 2 conditions met.
When visited node is traversed again. low_time[u] = min(low_time[u], low_time[v])
When backtrack on dfs do update low_time, low_time[u] = min(low_time[u], low_time[v])
5) After backtrack completed, and update on low_time completed, see adj node low_time is greater than current
node low_time. This is possible since node and adj node are not on same component.
If above example node 4 have 1 as low time and node 5 adj to 4 have 5.
6) Update bridge with node and adjacent node list, [source, adj], if met on above condition.
7) Start the DFS in main function with dfs(node, -1), starting node 0 considered parent -1.
8) Return bridge count
Time Complexity: O(E+V)
Space Complexity: O(V)
"""
import collections
from typing import List


class Solution:
    time = 1
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.time = 1
        bridges = []
        adj_list = collections.defaultdict(list)
        low_time = [-1] * n
        insert_time = [-1] * n

        def dfs(node, parent):
            insert_time[node] = low_time[node] = self.time
            self.time += 1

            for adj_node in adj_list[node]:
                if adj_node == parent: continue
                # -1 means it is not visited yet
                if insert_time[adj_node] == -1:
                    dfs(adj_node, node)
                    low_time[node] = min(low_time[node], low_time[adj_node])
                    # this means node and adj_node are not in same component 
                    # or adj node can't reach back to parent node
                    if low_time[adj_node] > insert_time[node]:
                        bridges.append([node, adj_node])
                else:
                    # see if other path exist to make the node reach back to parent
                    low_time[node] = min(low_time[node], low_time[adj_node])
        # build adj list
        for source, dest in connections:
            adj_list[source].append(dest)
            adj_list[dest].append(source)
        dfs(0, -1)
        return bridges
    
# Testing
sol = Solution()
print(sol.criticalConnections(5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]))
print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
