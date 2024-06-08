# Graph

Common patterns: https://youtu.be/utDu3Q7Flrw?si=blsv2zAu3qLoIQhY

Graphs are a fundamental data structure in computer science, used to model pairwise relations between objects. A graph consists of nodes (vertices) and edges (lines connecting the nodes). Graphs are widely used in various algorithms and have numerous applications in different fields. Here are some key uses of graphs in the context of data structures and algorithms:

- Representation of Networks:

Social Networks: Nodes represent users, and edges represent relationships (friendships, followers).
Computer Networks: Nodes represent computers or routers, and edges represent connections between them.
Transportation Networks: Nodes represent intersections or stations, and edges represent roads, railways, or flight paths.

- Pathfinding Algorithms:

Shortest Path: Algorithms like Dijkstra's and Bellman-Ford find the shortest path between nodes in a weighted graph.
A*: A* is a heuristic-based algorithm used for finding the shortest path, commonly used in game development and robotics.
Floyd-Warshall: This algorithm finds shortest paths between all pairs of nodes in a graph.

- Traversal Algorithms:

Depth-First Search (DFS): Explores as far as possible along each branch before backtracking, useful for pathfinding and detecting cycles.
Breadth-First Search (BFS): Explores all neighbors at the present depth before moving on to nodes at the next depth level, useful for shortest path in unweighted graphs and finding connected components.

- Minimum Spanning Tree:

Kruskal's Algorithm: Finds the minimum spanning tree (MST) of a graph, which connects all nodes with the minimum possible total edge weight.
Prim's Algorithm: Another MST algorithm that builds the tree starting from an arbitrary node and adding the cheapest possible connection.

- Cycle Detection:

Detecting cycles in a graph is crucial for problems in scheduling, dependency resolution, and deadlock detection. DFS-based methods are commonly used for cycle detection.

- Topological Sorting:

Applied to directed acyclic graphs (DAGs), topological sorting orders the nodes such that for every directed edge from node u to node v, u comes before v. This is useful in scheduling tasks, resolving symbol dependencies in compilers, and more.

- Connectivity and Components:

Connected Components: Identifying connected components in an undirected graph helps in understanding the structure of the graph.
Strongly Connected Components: In directed graphs, algorithms like Tarjan's or Kosaraju's identify strongly connected components, which are subgraphs where every node is reachable from every other node.

- Flow Networks:

Max Flow: Algorithms like Ford-Fulkerson and Edmonds-Karp find the maximum flow in a flow network, useful in network routing, bipartite matching, and circulation problems.

- Graph Coloring:

Assigning colors to graph nodes such that no two adjacent nodes share the same color. This is used in scheduling problems, register allocation in compilers, and map coloring.

- Planarity Testing:

Determining if a graph can be drawn on a plane without edges crossing, with applications in circuit design and geography.

References: https://www.youtube.com/playlist?list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI
