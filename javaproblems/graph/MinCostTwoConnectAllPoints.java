package graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

class AdjacencyPair {

    int node;
    int distance;

    AdjacencyPair(int node, int distance) {
        this.node = node;
        this.distance = distance;
    }
}

public class MinCostTwoConnectAllPoints {

    static HashMap<Integer, ArrayList<AdjacencyPair>> getAdjacencyList(int[][] points) {
        HashMap<Integer, ArrayList<AdjacencyPair>> adjacencyList = new HashMap<>();
        for (int indexI = 0; indexI < points.length; indexI++) {
            adjacencyList.putIfAbsent(indexI, new ArrayList<AdjacencyPair>());
            int x1 = points[indexI][0], y1 = points[indexI][1];
            for (int indexJ = indexI + 1; indexJ < points.length; indexJ++) {
                adjacencyList.putIfAbsent(indexJ, new ArrayList<AdjacencyPair>());
                int x2 = points[indexJ][0], y2 = points[indexJ][1];
                int distance = Math.abs(x1 - x2) + Math.abs(y1 - y2);
                adjacencyList.get(indexI).add(new AdjacencyPair(indexJ, distance));
                adjacencyList.get(indexJ).add(new AdjacencyPair(indexI, distance));
            }
        }
        return adjacencyList;
    }

    static int minCostTwoConnectAllPoints(int[][] points) {
        int cost = 0;
        boolean[] visited = new boolean[points.length];
        HashMap<Integer, ArrayList<AdjacencyPair>> adjacencyList = getAdjacencyList(points);
        PriorityQueue<AdjacencyPair> minHeap = new PriorityQueue<>((x, y) -> x.distance - y.distance);
        minHeap.add(new AdjacencyPair(0, 0));
        int visitedCount = 0;
        while (minHeap.size() > 0 && visitedCount < points.length) {
            AdjacencyPair pair = minHeap.poll();
            if (visited[pair.node]) {
                continue;
            }
            visited[pair.node] = true;
            cost += pair.distance;
            visitedCount++;

            for (AdjacencyPair adjPair : adjacencyList.get(pair.node)) {
                if (!visited[adjPair.node]) {
                    minHeap.add(adjPair);
                }
            }
        }
        return cost;
    }

    public static void main(String args[]) {
        int result = minCostTwoConnectAllPoints(new int[][]{{0, 0}, {2, 2}, {3, 10}, {5, 2}, {7, 0}});
        int result1 = minCostTwoConnectAllPoints(new int[][]{{3, 12}, {-2, 5}, {-4, 1}});
        System.out.println(result);
        System.out.println(result1);
    }
}
