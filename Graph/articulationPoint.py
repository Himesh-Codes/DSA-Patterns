"""
Articulation Point - I
Difficulty: Hard
https://www.geeksforgeeks.org/problems/articulation-point-1/1

Given an undirected connected graph with V vertices and adjacency list adj. 
You are required to find all the vertices removing which (and edges through it)
 disconnects the graph into 2 or more components and return it in sorted manner.
Note: Indexing is zero-based i.e nodes numbering from (0 to V-1). 
There might be loops present in the graph.

Example 1:
Output:{1,4}
Explanation: Removing the vertex 1 will
discconect the graph as-
Removing the vertex 4 will disconnect the
graph as-

Articulation Point
--------------------
It is the node which can remove to make the graph split into 2 or more components.
Using the same Tarjan's algo, but with little modification.

https://www.youtube.com/watch?v=j1QDfU21iZk

Intuition
----------
If we are able to group nodes with the low visit time, basically low_time is the 
insertion time of starting point of a graph component and see if we have multiple starting point in graph.
Usually one starting/ending node for one component and other starting/end node point for other component 
connecting first component.
Then removal of the connection point by seeing low[adjacent node] >= insertion[node],
ie, node can be either starting of that component if low[adjacent node] == insertion[node]
eg: 1 ----- 2 ----- 3
            |       |
            |       |
            ------- 4
Here 2 is starting point of compoent (2,3,4)


else node can be the connection point to starting of other component. low[adjacent node] > insertion[node]
eg: 1 ----- 2 ----- 3 ----- 5
                    |       |
                    |       |
                    ------- 4
Here 2 is connecting point of compoent (3,4,5)

And also origin point of DFS assume 0 have multiple children then it is an articulation point
eg: 1 ----- 0 ----- 3 ----- 5
            |       |       |
            |       |       |
            2        ------- 4

Conditions for finding
------------------
1) Create a insertion_time[] list, with the time of visit on each node. (initially -1)
2) lowest_time[] list should be updated with adjacent nodes, once backtrack, but not from it's parent node.

3)And from a visited node, we will not update with low_time of visited node like in bridges.
Rather we will update the low_time of node with insert_time of visited node.
low_time[u] = min(low_time[u], insert_time[v]), this is because the v might be in other component and if
v is removed we can't reach to it's other adj nodes.
Via visited node is the connection going that means if visited node is removed no point the 2 components
are connected each other, ie why we took insertion_time rather than low_time.

4) If the low_time[adj] >= insert_time[node] && parent != -1. 
Here we updated a little variation from bridge, 
bridge is an edge we remove so if low_time[adj] > insert_time[node] was the condition,
because if adj node is not able to traverse back to parent node in other way shorter, that is a bridge.

5) Here we remove the node itself so if insertion_time[node] == low_time[adj], 
means that is the starting point of an SCC, so removing it we can split the graph.
Also we check parent is not -1, becuase graph starting node will have parent as -1, 
so removing 0 will not make any difference. Until and unless it have mutliple children

7) For origin point we can say if it has multiple children then update it as a articulation point.
Once every DFS done and came back to origin (here 0 have multiple children).

eg:     1 ----- 0 -------  3
                |          |
                |          |
        4 ----- 2 ---------^
        |       |
        |       |
        6 ----- 5

    Dryrun on above example
    -----------------------
    Here we do DFS(0,-1), since 0 is start node and parent as -1. Initialy insertion_time & low-time are -1.
    insertion_time = [1, -1, -1, -1, -1, -1, -1], low_time = [1, -1, -1, -1, -1, -1, -1]

    Next from 0 we move to adj nodes, node 1, DFS(1, 0) here we check current node parent is -1.
    Not in this case it is 0, and updates insertion and lowest time of node 1 as 2, since timer = 2 now.
    insertion_time = [1, 2, -1, -1, -1, -1, -1], low_time = [1, 2, -1, -1, -1, -1, -1]
    Since 1 have no other adj nodes we backtrack in DFS.

    While backtrack we can see node 0 have parent -1, so not updates low_time on backtrack since 0 is origin.

    Next DFS(2,0), update insertion_time = [1, 2, 3, -1, -1, -1, -1], low_time = [1, 2, 3, -1, -1, -1, -1]

    Next adj node of 2 is node 3 we do DFS(3,2).
    update insertion_time = [1, 2, 3, 4, -1, -1, -1], low_time = [1, 2, 3, 4, -1, -1, -1]

    Now from 3 we have one adj node ie, node 0, since 0 is already visited we here applies the different 
    rule rather than bridge case, 
    we see parent is not 0, since parent of 3 is 2 we continue.
    For visited node: low_time[3] = min(low_time[3], insert_time[0]) = 1
    updates, insertion_time = [1, 2, 3, 1, -1, -1, -1], low_time = [1, 2, 3, 1, -1, -1, -1]
    
    Now 3 have no other adj nodes.
    So backtrack, to 2, then while backtrack.
    For backtrack: low_time[2] = min(low_time[2], low_time[3]) = 1
    updates, insertion_time = [1, 2, 3, 4, -1, -1, -1], low_time = [1, 2, 1, 1, -1, -1, -1]

    Now 2 have other adj node 4, unvisited DFS(4, 2)
    updates, insertion_time = [1, 2, 3, 1, 5, -1, -1], low_time = [1, 2, 3, 1, 5, -1, -1]

    Now 4 have other adj node 6, unvisited DFS(6, 4)
    updates, insertion_time = [1, 2, 3, 1, 5, -1, 6], low_time = [1, 2, 3, 1, 5, -1, 6]

    Now 6 have other adj node 5, unvisited DFS(6, 5)
    updates, insertion_time = [1, 2, 3, 1, 5, 7, 6], low_time = [1, 2, 3, 1, 5, 7, 6]

    Now 5 have other adj node 2, visited already
    For visited node: low_time[5] = min(low_time[5], insert_time[2]) = 3
    this is because the 2 might be in other component and if 2 is removed we can't reach to 
    it's other adj nodes ie, 1.
    updates, insertion_time = [1, 2, 3, 1, 5, 3, 6], low_time = [1, 2, 3, 1, 5, 3, 6]

    Now backtrack to node 6,
    For backtrack: low_time[6] = min(low_time[6], low_time[5]) = 3
    updates, insertion_time = [1, 2, 3, 1, 5, 3, 3], low_time = [1, 2, 3, 1, 5, 3, 3]

    Now backtrack to node 4, same as in node 6
    updates, insertion_time = [1, 2, 3, 1, 3, 3, 3], low_time = [1, 2, 3, 1, 3, 3, 3]

*** Now backtrack to node 2, here come's the point
    we see that lowe_time[4] >= insertion_time[2], yes and parent != 1 ie, not the origin node.
    So add the articulation_point = [2].
    That means the 4 and it's adjacent nodes connected are started from node 2.
    So if node 2 removed it splitted to 2 components.

    Now backtrack to 0 from 2, parent is -1 so not consider any update.

    Once all DFS is done we have to check origin 0, has multiple children or adj nodes, then we
    add 0 to articulation_point = [2, 0].

Steps
------
1) Do DFS and update insertion_time and low_time.
2) Update low_time of a node on 2 conditions, and if parent is not -1 (exclude operations on origin node)
    And if adj_node is not parent.
    i) Reaching a adj node visited, low_time[node] = min(low_time[node], insert_time[adj])
    ii) Backtrack from DFS, low_time[node] = min(low_time[node], low_time[adj])
3)  If the low_time[adj] >= insert_time[node] && parent != -1, then do add the node to 
    articulation_points[].
5) Once DFS is completed for origin 0 here we have to check adj_list of 0 have more than 1 children
    If yes we add origin to articulation_points[].
6) Return articulation_points[]
"""     
import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        articulation_points = []
        return articulation_points
    
# Testing