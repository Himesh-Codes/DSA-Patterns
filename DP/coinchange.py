"""
Coin Change
Difficulty: Medium

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 
Solution
----------
Use of dynamic programming is optimised approach.
Since the amount can be in x axis of DP array and y axis with the coin

Steps
-----------
1) Create DP array initialise every value 0, and sum 0 with each coin as 0, 
since without selecting that coin the chances are 0.
2) If sum - coin > 0, then get the difference sum using same coin, add 1 to it because use of current coin.
Add 1 if and only if the count for differebce is greater than 0
3) Take the previous coin chances from left (ie, dp[coin-1][sum]), 
take min(dp[amount][[coin-1]), currentCount), as dp value.
4) Return the dp[amount][len(coin)-1] as the final calculated combinations results.

Solution (Optimised)
-------------------
Dynamic programming in bottom up approach.
Using 1D Dp array.

Steps
-------
1) Create 1D Dp array, with dp[0] as 0. Initialise with a maximum number float('inf')
2) Iterate through every coin for an amount and add the difference amount in difference >= 0, plus 1,
as current coin also added.
3) Take the minimum of current DP value and count calculated.
4) return dp[amount] if not floar('inf'), else return -1

Time Complexity: O(N*M)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for amount in range(1, amount+1):
            for coin in coins:
                if amount - coin >= 0:
                  dp[amount] = min(dp[amount-coin] + 1, dp[amount])
        return dp[amount] if dp[amount] != float('inf') else -1
       
    
# Testing
sol = Solution()
print(sol.coinChange([186,419,83,408], 6249))
print(sol.coinChange([1,2,5], 11))