"""
Longest Common Subsequence
Difficulty: Medium

Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with 
some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

Solution
------------
Using 2D DP method, to see the different subproblem.
Below example when we got a match with first letter text1 'a' and 'a' of text2, so we go diagonally in maxtrix,
so we can look into other subproblem
"bcde" and "ce" are, b & c are not matching now option is either go take "e" in text2 or "c" in text1.
So in matrix we need to go right(j+1), or down(i+1), and take max of the possibility.
He we get the 1 as result only when the both strings are iterated in all possible way that is last row and last col.
Here it is coordinate ("e", "e"), since it is match we add one. From there we will go up and left on iteration.
Since the chars in up ("d", "e"), not match it take max from (i+1, j+1), ie, 1 is answer.
Thus we build all dp matrix. And final result in dp[0][0], that is upper corner coordinate.
We need to traverse in bottom up approach to get this problem solved.

Matrix look like : text1 = "abcde" & text2 = "ace"
        a   c   e   " "
    a   3           0
    b       2       0
    c       2       0
    d           1   0
    e           1   0
    " "0    0   0

Steps
---------
1) We have to create a dp matrix with width(j) of text2 and height(i) of text1. And last row and last column will be
for empty char since the possibility of empty char is 0, we assign every coordinates in last row, column with 0.
2) Here the if we see match we will add 1 + value in corner/diagonal(i+1, j+1).
3) If not match found we will see the results from right and down coordinate traversal max(i+1, j+1).
4) The result will be returned in dp[0][0].

Time Complexity: O(N * M), len of text1 is N and len of text2 is M
Space Complexity: O(N * M), since dp matrix is of size N * M.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for index in range(0, len(text1)+1)] 

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]

# Testing
sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))