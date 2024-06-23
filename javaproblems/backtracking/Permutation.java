package backtracking;

import java.util.ArrayList;
import java.util.List;

public class Permutation {

    static List<List<Integer>> getPermutation(List<Integer> nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums.size() == 1) {
            result.add(nums);
            return result;
        }
        int size = nums.size();
        for (int index = 0; index < size; index++) {
            int idleElement = nums.remove(0);
            List<Integer> copyArr = new ArrayList<>();
            copyArr.addAll(nums);
            List<List<Integer>> perms = getPermutation(copyArr);

            for (List<Integer> perm : perms) {
                perm.add(idleElement);
            }
            result.addAll(perms);
            nums.add(idleElement);
        }
        return result;
    }

    public static List<List<Integer>> permute(int[] nums) {
        ArrayList<Integer> numbers = new ArrayList<>();
        for (int index = 0; index < nums.length; index++) {
            numbers.add(nums[index]);
        }
        return getPermutation(numbers);
    }

    public static void main(String[] args) {
        List<List<Integer>> result = permute(new int[]{1, 2, 3});
        System.out.println(result);
    }
}
