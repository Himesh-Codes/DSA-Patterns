"""
 Coin Change II
 Difficulty: Medium
 https://leetcode.com/problems/coin-change-ii/description/

 You are given an integer array coins representing coins of different denominations and 
 an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.


Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1

Solution
----------
Memoization using the DP is optimized way. Amount in Y axis and coins in x axis.
Since the chances with the previous coins and chances with difference amount are already might be calculated.

Steps
--------
1) Create DP array initialise every value 0, and sum 0 with each coin as 1, 
since without selecting that coin the chances are one.
2) If sum - coin > 0, then get the difference sum using same coin.
3) Add the previous coin chances from left (ie, dp[coin-1][sum]) also added into current sum, 
and then assign sum value.
4) Return the dp[amount][len(coin)-1] as the final calculated combinations results.
"""
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins)) for index in range(0, amount+1)]
        for index in range(0, len(coins)):
            dp[0][index] = 1

        for coinindex in range(0, len(coins)):
            for sumAmount in range(1, amount+1):
                currentSum = 0 if coinindex - 1 < 0 else dp[sumAmount][coinindex - 1]
                if sumAmount - coins[coinindex] >= 0:
                    currentSum += dp[sumAmount - coins[coinindex]][coinindex]
                dp[sumAmount][coinindex] = currentSum

        return dp[amount][len(coins)-1]

# Testing
sol = Solution()
print(sol.change(5, [1,2,5]))
print(sol.change(3, [2]))