"""
Number of Connected Components in an Undirected Graph
Difficulty: Medium
https://www.lintcode.com/problem/3651/

In this problem, there is an undirected graph with n nodes. 
There is also an edges array. Where edges[i] = [a, b] means that there is an edge between
node a and node b in the graph.

You need to return the number of connected components in that graph.
Example 1

Input:

3
[[0,1], [0,2]]
Output:

1
Example 2

Input:

6
[[0,1], [1,2], [2, 3], [4, 5]]
Output:

2

Solution Optimised (UNION FIND )
-----------
Find Forest Of Trees / Union find algorithm is the pattern to find the union of group of graph nodes toghether.

Parent array will have the note on the parent / start of each connected forest. 
eg: 0 ----  1            3
            |            |
            |            |
            2            4
- For a graph like above the parents of each node will be parent of itself, 
- considering the index as value of node and value as parent of node, 
ie, parent = [0,1,2,3,4]

- For optimisation of connecting components (adding always to root parent), rather than creating an linked list route, 
thusby reduce the height of the tree.

ie, After traversal of 2 , 2 will be connected to root parent 0 and one is already connected to root parent 0.

    0 -- 1
    |
    2
        
- Rank denotes the size of a connected components forest, initially it will be 1 for all nodes
ie, rank = [1,1,1,1,1]

Edge cases
-----------
- If the one node to edge to node traversal happen and we see that the source and destination node have same root parent, 
that means it is already connected in other way so no need to decrement from total nodes count. 

Steps
------
Two utility functions;

- FindParent (returns parent node): to get the root parent of the nodes. To just optimise the linear run time complexity we can do a stuff
ie, parent[node] = parent[parent[node]], considering the graph path as a linked-list, 
it assigns the grand parent of parent to the parent of node, to reduce linear runtime.
This won't fail even if the grand parent don't exist, since the node can be itself's parent.

- Union (return value 0/1 for success/unsuccess): to execute the merge operation of the two node, connected with an edge. 
Inside it calls find and merge the 2 given nodes.

- A for loop running on the edge and vertex to find and merge
- The rank of the parent is increasing with rank of child once we find a new node added to parent, ie, rank[p] += rank[c].

- For every node to edge to node travsersal eg:, 1---2, 
we have to take find the root parent doing a recursion DFS 
(where we can check until the parent of node is the node itself, ie, no more root parent search exist).
- And assign root parent as the parent of newly traversed node.

- Once the union operation is done the that is parent updated we decrement the component, from total nodes count
to return the connected components counts. (Initially let's say 5 nodes will be the individually connected components)

Time Complexity: O(E+V)
Space Complexity: O(V) where we store the rank and parent array of each nodes.

Solution DFS
------
We can do the DFS on the one of the node and traverse through all edges and visit the connected nodes.
Add the nodes visited into a visited array, and once one dfs completed we get one component.
Do DFS for all other unvisited nodes and find the components connected.

Time Complexity: O(E+V)

"""

from typing import List


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        parent = [item for item in range(n)]
        rank = [1] * n

        def find(node):
            while node != parent[node]:
                # optimisation of linear runtime
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def unionNodes(nodeOne, nodeTwo):
            parentOne, parentTwo = find(nodeOne), find(nodeTwo)

            # if both root parent same means already merged
            if parentOne == parentTwo:
                return 0
            
            # connnect the root parents according to the rank for union
            if rank[parentOne] > rank[parentTwo]:
                parent[parentTwo] = parentOne
                # size of parent increase with size of the child node
                rank[parentOne] += rank[parentTwo]
            else:
                parent[parentOne] = parentTwo
                # size of parent increase with size of the child node
                rank[parentTwo] += rank[parentOne]
            return 1

        connectNodesCount = n
        for source, destination in edges:
            connectNodesCount -= unionNodes(source, destination)
        return connectNodesCount
            


# Testing
sol = Solution()
print(sol.count_components(6, [[0,1], [1,2], [2, 3], [4, 5]]))