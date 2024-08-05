"""
Edit Distance
Difficulty: Medium/Hard
https://leetcode.com/problems/edit-distance/description/

Given two strings word1 and word2, return the minimum number of operations required to convert 
word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

Intuition
----------

We have to match the word1 to word2 by altering word1.
Thought process is if bottom up since if we know minimum operation to achieve the last element to make same
of word 2, we can say dp[n-1][n-1], then we could easily calculate what operation needed to calculate the
dp[n-2][n-2].

Intuition based on edge case with empty string for each char position for word1 and word2.

Input: word1 = "horse", word2 = "ros"
Let's say in above example what is the count of operation needed if from index 0 of "h"
if need to match word2 we need to say 5 delete operation needed in word1 .

Also in position of char "s", in word1, if need to match rest of the word2, we need to delete
2 word, so the empty string in position 4 , no of operations would be 2.
ie, len(rest_of_the_string) is the operations needed in each position.

eg:         r   o    s   " "
        h   3   3    4    5
        o   3   2    3    4
        r   2   2    2    3
        s   3   2    1    2
        e   3   2    1    1
       " "  3   2    1    0

       We mapped the word1 and word2 and empty string
       Assume if chars is empty in word 2 then 5 operations needed, like wise
       if word1 is empty then we need len(word2) as we need to copy everything.

       h o r s e    r o s
       ^            ^

       Index 0, i & j pointers on the word1 and word2 respectively, we have 3 options 
       r h o r s e    r o s
         ^              ^
       - Insert on word1: Since we insert the same char on word2 we can move to (i, j+1).
        Since we insert on word1 now we see char in j pointer already matching but i pointer char in word1
        now need to match with j+1.
         No:of operation 1.

         o r s e    r o s
         ^            ^
       - Delete on word1: If delete we can move to next char in word1, comparing with same char in word2
         do to next char in word1 match with same char in j (i+1, j)
            No:of operation 1

         r o r s e    r o s
           ^            ^

       - Replace on word1: Replace a char in word1 we will move to other char of the both strings since
       current both chars are same. (i+1, j+1). No:of operation 1

        r o r s e    r o s
            ^            ^

       - If both are equal we need to move (i+1, j+1), and number of operations is 0. 
       (Before word1 "o" was equal with word2 "o".)

    Identification of subproblems in DP
    ------------------------------------
    Since the word1 is to be equal to word2 by left to right char by char, the rightmost char is
    end we can see dp[N-1][N-1] is the first point to calculate.
    If both right most char same we can say dp[n][n] = (i+1, j+1), it will be mostly 0.
    If two chars not same see min (dp[i][j+1], dp[i+1][j], dp[i+1][j+1]) and add 1 since it is as operation.
    Subproblem analysis is dp[i][j] depends on [i][j+1], [i+1][j], [i+1][j+1] values.

Solution
----------
https://www.youtube.com/watch?v=XYi2-LPrwm4

2D DP with the bottom up approach.
word1 on the x axis and word 2 on the y axis.

"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]  * (len(word2)+1) for _ in range(len(word1)+1)] 
        
        # adding the edge cases of empty string
        for index in range(len(word1), -1, -1):
            dp[index][len(word2)] = len(word1) - index

        for index in range(len(word2), -1, -1):
            dp[len(word1)][index] = len(word2) - index


        # bottom up DP approach
        for indexI in range(len(word1)-1, -1, -1):
            for indexJ in range(len(word2)-1, -1, -1):
                if word1[indexI] == word2[indexJ]:
                    dp[indexI][indexJ] = dp[indexI+1][indexJ+1]
                else:
                    dp[indexI][indexJ] = 1 + min(dp[indexI+1][indexJ+1], dp[indexI+1][indexJ], dp[indexI][indexJ+1])
        
        return dp[0][0]

# Testing 
sol = Solution()
print(sol.minDistance("horse", "ros"))
