package array;

import java.util.HashSet;
import java.util.Set;

public class LongestConsecutiveSeq {
    static int longestConsecutiveSequence(int[] nums){
        int maxSequenceLen = 0;
        if (nums.length == 0){
            return 0;
        }

        // put all the array elements into List/Set for access of APIs
        Set<Integer> numbers = new HashSet<>();
        
        for(int num: nums){
            numbers.add(num);
        }

        for (int number : numbers){
            Set<Integer> sequence = new HashSet<>();
            if (!numbers.contains(number-1)) {
                while(numbers.contains(number)){
                    sequence.add(number);
                    number += 1;
                }
                maxSequenceLen = Math.max(maxSequenceLen, sequence.size());
            }
        }

        return maxSequenceLen;
    }
    public static void main(String args[]){
        // Testing
        int result = longestConsecutiveSequence(new int[]{100,4,200,1,3,2});
        int result1 = longestConsecutiveSequence(new int[]{300,2,400,4,1});
        System.out.println(result);
        System.out.println(result1);
    }
}
