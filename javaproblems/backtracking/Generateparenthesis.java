package backtracking;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

public class Generateparenthesis {

    static List<String> combination = new ArrayList<>();

    static void recurse(int openCount, int closedCount, int n, ArrayDeque<String> stack) {
        if (openCount == closedCount && closedCount == n) {
            String parenthesis = String.join("", stack);
            combination.add(parenthesis);
        }
        if (openCount < n) {
            stack.add("(");
            recurse(openCount + 1, closedCount, n, stack);
            stack.pollLast();
        }

        if (openCount > closedCount) {
            stack.add(")");
            recurse(openCount, closedCount + 1, n, stack);
            stack.pollLast();
        }

    }

    static List<String> generateParenthesis(int n) {
        combination = new ArrayList<>();
        ArrayDeque<String> stack = new ArrayDeque<>();
        recurse(0, 0, n, stack);
        return combination;
    }

    public static void main(String[] args) {
        List<String> result = generateParenthesis(1);
        for (String str : result) {
            System.out.println(str);
        }
        List<String> result1 = generateParenthesis(3);
        for (String str : result1) {
            System.out.println(str);
        }
    }
}
