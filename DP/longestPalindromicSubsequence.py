"""
Longest Palindromic Subsequence
Difficulty: Medium
https://leetcode.com/problems/longest-palindromic-subsequence/description/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.

Solution (BruteForce)
----------
Create all subsequences using DFS (O(N2)) and see it is a palindrome (O(N)), total O(N3) complexity.
Calculate len and return max len.

https://www.youtube.com/watch?v=bUr8cNWI09Q

Spread wide operations with DFS since subsequences can be of skipping any chars.
Using the recursion, if i or j is out of bounds we are not suppose to equate anything so return 0/
If match occurs we spread wide we ahve 2 cases
- If i & j are same means it's on same char so add len 1 else, it's in different char so add 2.
- Spread wide (i-1, j+1)
Else if no match we do DFS (i, j+1), (i-1, j), and take the max value from both DFS.
Do for both odd and even palindrome case.
Time Complexity: O(2^N), since odd and even cases are there.

Optimise Time Complexity (O(N2))
---------------------------------
Using a cache with hashmap of key as pair of (i,j) and value as the length so far.
We can add and retrieve length from cache.

Solution(Optimized) : LCS - Longest Common Subsquence 2D DP 
-----------------------------------------------------------
This trick relies on how we determine a palindrome, and palindrome string will be equal to reverse of the same string.
Here we need to find the maximum long palindrome subsequence, considering is same as finding longest common subsequence of 2 strings.
We do 2D DP in bottom-up approach to calculate the maximum possible equal subsequence of each chars in 2 strings in bottom-up manner.

We can consider same approach here string1 is the input string itself and string2 is the reverse of string.
And from these two get the longest common subsequence length.

Time Complexity: O(N2)
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        reverse = s[::-1]
        dp = [[0] * (n+1) for _ in range(n+1)] 

        # bottom up approach
        for indexI in range(n-1, -1, -1):
            for indexJ in range(n-1, -1, -1):
                if s[indexI] == reverse[indexJ]:
                    dp[indexI][indexJ] = 1 + dp[indexI+1][indexJ+1]
                else:
                    # max of right subequence ie, same string , down ie, second string
                    dp[indexI][indexJ] = max(dp[indexI][indexJ+1], dp[indexI+1][indexJ])

        return dp[0][0]
    
# Testing
sol = Solution()
print(sol.longestPalindromeSubseq("bbbab"))
print(sol.longestPalindromeSubseq("cbbd"))