package graph;

import java.util.LinkedList;
import java.util.Queue;

class Position {

    int x;
    int y;

    Position(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class StepsByKnight {

    public static int minStepToReachTarget(int KnightPos[], int TargetPos[], int N) {
        int steps = 0;
        boolean[][] visited = new boolean[N][N];
        Position start = new Position(KnightPos[0] - 1, KnightPos[1] - 1);
        Position target = new Position(TargetPos[0] - 1, TargetPos[1] - 1);

        if (start.x == target.x && start.y == target.y) {
            return 0;
        }

        Queue<Position> queue = new LinkedList<>();
        queue.add(start);
        visited[start.x][start.y] = true;

        int[][] directions = {{-2, -1}, {-2, 1}, {-1, 2}, {1, 2}, {-1, -2}, {1, -2}, {2, -1}, {2, 1}};

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int index = 0; index < size; index++) {
                Position popPos = queue.poll();
                for (int[] coordinate : directions) {
                    int newX = popPos.x + coordinate[0];
                    int newY = popPos.y + coordinate[1];
                    if (newX == target.x && newY == target.y) {
                        return steps + 1;
                    }
                    if (newX >= 0 && newY >= 0 && newX < N && newY < N && !visited[newX][newY]) {
                        queue.add(new Position(newX, newY));
                        visited[newX][newY] = true;
                    }
                }
            }
            steps++;
        }
        return -1;
    }

    public static void main(String[] args) {
        int result = minStepToReachTarget(new int[]{4, 5}, new int[]{1, 1}, 6);
        int result1 = minStepToReachTarget(new int[]{6, 1}, new int[]{2, 4}, 7);
        System.out.println(result);
        System.out.println(result1);
    }
}
