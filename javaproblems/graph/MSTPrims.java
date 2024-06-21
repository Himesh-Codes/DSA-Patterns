/*
   Minimum Spanning Tree
   ----------------------

 * Given a weighted, undirected, and connected graph with V vertices and E edges, 
 * your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. 
 * The graph is represented by an adjacency list, where each element adj[i] is a vector containing pairs of integers. 
 * Each pair represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.
 * 
 * Difficulty: Medium
 * 
 * https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=minimum-spanning-tree
 * 
 * Example 1:
 * Input:
    3 3
    0 1 5
    1 2 3
    0 2 1

    Output:
    4

    Explanation:
    The Spanning Tree resulting in a weight of 4, is got from the route 0 -- 2 --- 1, 0 to 2 have weight 1, 2 to 1 have weight 3, 
    now total 4 for all nodes connected minimum spanning tree.
 * 
 * Example 2:
 * Input:
    2 1
    0 1 5
    Output:
        5
    Explanation:
        Only one Spanning Tree is possible
        which has a weight of 5.
 * 
 * Solution (Prim's Alogrithm) Time Complexity: O(V2logE)
 * ---------------------------
 *  1) Find all the edges with adjancency matrix.
    2) Keep a visited array to track visited item, and a min-heap (priority queue) for add items during BFS.
    3) Min-heap used for find the minimum edge from current node to adjacent node and connect them toghether.
    4) Stops the loop until the all nodes are connected, by checking visited nodes count is equal to total nodes.
 * 
 * Steps
 * ----------
 * 1) Create adj list on each nodes with Pair(node, weight)
 * 2) We only keep pair of Pair(node, weight) in the heap. Since we don't need a parent child track.
 * ie, {{0,3,6}, {0,1,1}, {1,3,1}}, here while building MST source 0 will take 0--1 connection since weight is lesser in heap of adj nodes of 0, {(1,1),(3,6)} is 1.
 * Next after we take 1 into MST we add it's adj node {(3,6), (3,1)}, here we take 3 with weight 1 connected to  1 --- 3, 
 * but here we can assume we 1,3 is connected to it's super parent 0 , 1----0 -----3.
 * We only care about the minimum cost of the spanning tree (here cost will be 2)
 * 
 * 3) Becuase of same above reason we don't need to flush the heap as we add new dependencies of new adjancent node.
 * 4) We start with a random node and add the distance as 0 for it.
 * 
 * Space Complexity: O(E+V), as O(E) for min-heap, O(V) for visited array and adjacency list.
 */
package graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

class Pair {

    int node;
    int weight;

    Pair(int node, int weight) {
        this.node = node;
        this.weight = weight;
    }

}

public class MSTPrims {

    static HashMap<Integer, ArrayList<Pair>> getAdjacencyList(int[][] adj) {
        HashMap<Integer, ArrayList<Pair>> adjList = new HashMap<>();
        for (int[] adjElement : adj) {
            int nodeOne = adjElement[0], nodeTwo = adjElement[1], edgeWeight = adjElement[2];
            adjList.putIfAbsent(nodeOne, new ArrayList<>());
            adjList.putIfAbsent(nodeTwo, new ArrayList<>());
            adjList.get(nodeOne).add(new Pair(nodeTwo, edgeWeight));
            adjList.get(nodeTwo).add(new Pair(nodeOne, edgeWeight));
        }
        return adjList;
    }

    static int getMSTSumOfWeights(int V, int E, int[][] adj) {
        int total = 0;
        HashMap<Integer, ArrayList<Pair>> adjList = getAdjacencyList(adj);
        PriorityQueue<Pair> heap = new PriorityQueue<>((x, y) -> x.weight - y.weight);
        boolean[] visited = new boolean[V];
        int visitedCount = 0;
        heap.add(new Pair(0, 0));
        while (!heap.isEmpty() && visitedCount < V) {
            Pair nodePair = heap.poll();
            if (visited[nodePair.node]) {
                continue;
            }
            visited[nodePair.node] = true;
            total += nodePair.weight;
            visitedCount++;
            for (Pair adjPair : adjList.get(nodePair.node)) {
                if (!visited[adjPair.node]) {
                    heap.add(adjPair);
                }
            }
        }

        return total;
    }

    public static void main(String[] args) {

        int result = getMSTSumOfWeights(3, 3, new int[][]{{0, 1, 5}, {1, 2, 3}, {0, 2, 1}});
        System.out.println(result);
    }

}
