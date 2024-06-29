"""
Strongly Connected Components (SCC)
Difficulty: Medium
https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo

Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges,
Find the number of strongly connected components in the graph.

Solution (Kosaraju's Algo)
--------------------------
https://www.youtube.com/watch?v=R6uoSjZ2imo

The thought process:
We can do a DFS and see what all nodes are interconnected in graph or there is a path back to same vertex.
But we can see the each vertex form a SCC of it's own.
And SCC's are connected each other, SCC1 -> SCC2 -> SCC3 -> SCC4 etc... So how do we stop this.
The intuition is if the vertices are connected each other to form an SCC, 
1)even if it's edges are "REVERSED", the same path will be there. But the connection to next SCC will break.

eg:  0 <---- 2 ------> 3  -------> 4 -------<----->  7
    |        ^                     |          ^
    |        |                     |          |
    V        |                     V          |
    1 -------                      5 -------> 6

    Here; SCC1: [0,1,2], SCC2: [3], SCC3: [4,5,6], SCC4: [7]
    And we can see connections within SCC's SCC1 -> SCC2 -> SCC3 -> SCC4

As our solution says, if we reverse all edges;

    0 ---->  2 <----- 3  <-------  4 -------  <----  7
    ^        |                     ^          |
    |        |                     |          |
    |        |                     |          V
    1 <------                      5 <------- 6

    Now the SCC's are SCC1: [0,1,2], SCC2: [3], SCC3: [4,5,6], SCC4: [7]
    But connection from SCC1 to 3 is gone, like SCC2 to 7 is gone, and 3 & 7 are independent SCC's

Other issue now is where to start to get SCC's correctly.
We know SCC1 to 3 connection is lost, but in reverse if someone start from 3 it can go to SCC1.
So how to stop this.
2) Now solution is before we reverse graph need to see finishing time of each vertex.
That mean while DFS from a vertex when it will reach the maximum end node and reachback.
So the last finish (first in FINISH STACK), will be in SCC1 and first to start, to avoid connect in 
between 2 SCC's.

In above example while we traverse from 0 vertex, the path will be following
We will keep a visit array,
DFS(0) --> DFS(1) --> DFS(2) from DFS(2) we see edge to 0, but now in our visited array [0,1,2]
0 is already present so we don't traverse, but DFS(2) --> DFS(3) ---> DFS(4) --> DFS(5) --> DFS(6)
Now DFS(6) go to node 4, in our visited array [0,1,2,3,4,5,6], 4 is already visited,
so now DFS(6) --> DFS(7), now DFS(7) have no other node to visit, so it is last node.
Means it should be in our last SCC, ie, SCC4 here.

Now going backrack in DFS we add to FINISH STACK [7, 6, 5, 4, 3, 2, 1, 0].
We know now 0 is top of stack and it should be in SCC1 or first to traverse.

So now need to DFS in reverse graph in FINISH STACK top to bottom order.
And we maintain a visited array to track.
Now we pop 0 and do DFS, so 0 ---> 2 ---> 1, and from 2 it got to 0, in our visited array [0,2,1]
so we end up here, from to in REVERSE GRAPH no edge is there.
SCC1: [0,1,2], then now in stack 1, 2 is already visited.
SCC2: [3], because 3 have edge go back to 2 that is already visited.
This because of that we traversed in correct order.
Now we pop 4, and do DFS, so 4 --> 6 --> 5, and from 5 it got to 4. in our visited array [0,2,1,4,6,5] 
SCC3: [4,6,5], pop 6,5 already visited no actions.
At end of stack it is 7 poped
SCC4: [7], so now we got answer.


Steps
-----
1) Do a DFS on the vertices and build FINISH stack. 
2) Keep a visited array to not to traverse again and DFS go until the end vertex.
3) While backtrack we add to FINISH stack, in that order.
4) Now we need to do reverse all edges, now get a REVERSED graph.
5) Then do a DFS to find SCC's in FINISH stack top to bottom order.
6) Now add the resultant track into result array.

Time Complexity: O(V+E).
Auxiliary Space: O(V+E).

"""
import collections


class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        numberOfScc = 0
        finishStack = []
        adjacencyList = collections.defaultdict(list)
        
        # create adj list
        for source, dest in adj:
            adjacencyList[source].append(dest)
        
        # create sorted finish stack
        finishStackVisited = []
        def finishStackDFS(vertex):
            finishStackVisited.append(vertex)
            if vertex not in adjacencyList:
                finishStack.append(vertex)
                return
            for dest in adjacencyList[vertex]:
                if dest not in finishStackVisited:
                    finishStackDFS(dest)
            finishStack.append(vertex)
        finishStackDFS(0)
        
        # reverse graph adj list
        reverseAdjList = collections.defaultdict(list)
        for sourceVertex in adjacencyList:
             for adjDest in adjacencyList[sourceVertex]:
                reverseAdjList[adjDest].append(sourceVertex)

        # final DFS 
        visited = []
        def dfs(vertex):
            visited.append(vertex)
            if vertex not in reverseAdjList:
                return
            for dest in reverseAdjList[vertex]:
                if dest not in visited:
                    dfs(dest)
        
        while finishStack:
            vertex = finishStack.pop()
            if vertex not in visited:
                dfs(vertex)
                numberOfScc += 1
        return numberOfScc

# Testing
edges = [[1, 0], [0, 2],[2, 1], [0, 3],[3, 4]]
edges1 = [[0, 1], [1, 2],[2, 0], [2, 3],[3, 4], [4, 5], [5, 6], [6, 7], [4, 7], [6, 4]]
sol = Solution()
print(sol.kosaraju(5, edges1))
print(sol.kosaraju(5, edges))
