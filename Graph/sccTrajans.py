"""
Strongly Connected Components (SCC)
Difficulty: Medium
https://www.geeksforgeeks.org/problems/strongly-connected-component-tarjanss-algo-1587115621/1?page=2&category=Graph&company=Amazon&difficulty=Medium,Hard&sortBy=submissions

Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges,
Find the number of strongly connected components in the graph.

SCC's (Tarjans Algo)
------
Details description in bridges in graph question.
https://www.baeldung.com/cs/scc-tarjans-algorithm
https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

We will need to see the somewhat same steps. But use a stack to find the vertices in SCC.
1) Do DFS from the first node.
2) Add the insertion time as whenever we find the node in DFS and also initiate lowest time as same as
insertion time.
3) Once on DFS when dfs(u) goto dfs(v), where v is already visited and in dfs stack, 
then we see it is a backedge, then we compare,
lowest_time[u] = min(lowest_time[u], insertion_time[v]).
Otherwise it is a cross edge between 2 SCCs.
4) While backtrack from the vertex w to vertex v, we need to see the 
lowest_time[v] = min(lowest_time[v], lowest_time[w]).
5) On backtrack / once we see the DFS is completed for a node including it's adjacent nodes and see if
it's insertion time and low time are equal, if that is equal it means it is the starting node of SCC.
So we pop out all elements in stack until our parent node reached (ie, insertion_time == lowest_time.)
5) Atlast the SCC are interconnected each other and we can see the lowest_time of all SCC are same.

eg:  1 -------> 2 ----------
     |          |           |
     |          |           |
     |          V           V
     ^ <-------- 3 -------> 4

     Here SCC's are [1,2,3][4]
    
    On DFS we have stack [1,2,3,4], low = [1,2,3,4] insert = [1,2,3,4]
    then we see once the DFS completed for 4, low == insert of 4 node
    So it is a SCC starting, when we pop until node 4, we get scc = [[4]]
    
    Now we backtrack on 3 then visit 1, so now the 1 is in the stack we know the 1 is visited and it
    is in stack that means it is a back edge. So update low = [1,2,1,4] insert = [1,2,1,4]

    Now to node 2, as we backtrack we see the low and insertion, 
    So update low = [1,1,1,4] insert = [1,1,1,4], 

    * From 2 there is one more edge, but this is the question do we need to consider this, no because
    it is a cross edge not in stack, ie, it is the edge connecting SCC1 --- SCC2


Time Complexity: O(E+V)
Space Complexity: O(V)
"""

class Solution:
    time = 1

    #Function to return a list of lists of integers denoting the members 
    #of strongly connected components in the given graph.
    def tarjans(self, V, adj):
        lowest_time = [float('inf')] * V
        insertion_time = [float('inf')] * V
        stack = []
        scc = []
        stackMember = [False] * V

        def dfs(node, stack: list):
            insertion_time[node] = lowest_time[node] = self.time
            self.time += 1
            # boolean array to reduce linear complexity
            stackMember[node] = True 
            stack.append(node)

            for adj_node in adj[node]:
                if insertion_time[adj_node] == float('inf'):
                    dfs(adj_node, stack)
                    lowest_time[node] = min(lowest_time[adj_node],lowest_time[node])
                # we need to find the backedge or not, if visiting again same stack member
                elif stackMember[adj_node]:
                    lowest_time[node] = min(insertion_time[adj_node],lowest_time[node])

            # while we reach the vertex pop to get SCC
            pop = -1
            if lowest_time[node] == insertion_time[node]:
                scc_item = []
                while(pop != node):
                    pop_node = stack.pop()
                    scc_item.append(pop_node)
                    stackMember[pop_node] = False
                    pop = pop_node
                scc.append(scc_item)

        for node in range(V):
            if insertion_time[node] == float('inf'):
                dfs(node, stack)
        
        return scc

# Testing
sol = Solution()
print(sol.tarjans(5, [[2, 3], [0], [1], [4], []]))
sol1 = Solution()
adj = [[1], [2],[0, 3], [4], [5,7], [6], [7,4], [7]]
print(sol1.tarjans(8, adj))