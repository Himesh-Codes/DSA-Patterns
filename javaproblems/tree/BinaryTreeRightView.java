package tree;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/*
 * Have 2 Approaches
 * 1- Is using a queue and doing BFS (Time Complexity: O(n2), Space Complexity: O(N))
 * 2- Doing recursion in order right() and left(), so after right the recursion go to right,
 * If both all null return to root parent. 
 * (Time Complexity: O(n2), Space Complexity: O(N))
 */
public class BinaryTreeRightView {

    static List<Integer> bfs(TreeNode root, List<Integer> rightSideElements) {
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.push(root);
        while (!queue.isEmpty()) {
            TreeNode lastNode = queue.peekLast();
            rightSideElements.add(lastNode.val);
            Deque<TreeNode> childQueue = new ArrayDeque<>();
            while (!queue.isEmpty()) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    childQueue.add(node.left);
                }
                if (node.right != null) {
                    childQueue.add(node.right);
                }
            }
            queue = childQueue;
        }
        return rightSideElements;
    }

    static void recursion(int level, TreeNode root, List<Integer> rightSideElements) {
        if (root == null) {
            return;
        }
        // if size is same means we need to add one more in this level
        if (rightSideElements.size() == level) {
            rightSideElements.add(root.val);
        }
        // do recursion first on rightmost and then go back to left and then root and do same backwards
        recursion(level + 1, root.right, rightSideElements);
        recursion(level + 1, root.left, rightSideElements);

    }

    static List<Integer> rightSideView(TreeNode root) {
        List<Integer> rightSideElements = new ArrayList<>();
        if (root == null) {
            return rightSideElements;
        }
        bfs(root, rightSideElements);
        return rightSideElements;
    }

    static List<Integer> recursiveRightSideView(TreeNode root) {
        List<Integer> rightSideElements = new ArrayList<>();
        if (root == null) {
            return rightSideElements;
        }
        recursion(0, root, rightSideElements);
        return rightSideElements;
    }

    public static void main(String[] args) {
        TreeNode lev1R = new TreeNode(3);
        TreeNode root = new TreeNode(1, null, lev1R);

        List<Integer> result = rightSideView(root);
        System.out.println(result);
        List<Integer> result1 = recursiveRightSideView(root);
        System.out.println(result1);
    }
}
