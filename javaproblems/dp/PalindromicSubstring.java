package dp;

public class PalindromicSubstring {
    static int palindromicSubtring(String s){
        int palindromes = 0;
        for(int index=0; index<s.length(); index++){
            palindromes += spreadCheck(index, index, s);
            palindromes += spreadCheck(index, index+1, s);
        }
        return  palindromes;
    }

    static int spreadCheck(int left, int right, String s){
        int palindromeCount = 0;
        while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
            palindromeCount += 1;
            left -= 1;
            right += 1;
        }
        return palindromeCount;
    }
    public static void main(String args[]){
        int result = palindromicSubtring("abc");
        int result1 = palindromicSubtring("aaa");
        System.out.println(result);
        System.out.println(result1);
    }
}
