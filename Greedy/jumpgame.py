"""
Jump Game
Difficulty: Medium

https://leetcode.com/problems/jump-game/description/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array 
represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Solution (Brute Force)
----------
Brute Force: approach is using a DFS and try all the combination of possible path through step.
Time = O(N^M) exponential Space = O(1)
Intuition
----------
Simply recursively traverse all possible path and if we can reach the end index

Steps
-------
In recursion if reach final index or greater, then return TRUE
Else after execute all possible step jumps on an index, 
If DFS(step) is True then return True
Else after all return FALSE

Solution (Optimised)
----------
BottomUp DP: Backward traversal and memoization of each traveled step.
Time = O(N2) Space = O(N)
Intuition
----------
We traverse from end, keeping a DP array with DP[-1] end index marked True all others as False.
While iterate from back we will find any steps from current index can reach a True step index.

Steps
-------
- Create a DP = [False] * N and make end index marked as True
- While iterarte back we will see any step jump of current index can reach a good step True 
- If yes mark current Index as True in DP, else mark it as False
- Continue until index 0 and see if Index 0 is True or False


Solution (Optimised)
----------
Greedy Approach: Backward traversal and see any jump from current index can cross last_good_step.
If YES update last_good_step as current index else continue iteration back
Time = O(N) Space = O(1)
Intuition
----------
So on jump what is our main target ie; to reach end index. If we traverse from back initial last_good_step is index N
Iterate back and see any jump on index(n-1, n-2, n-3 ..... 0) can reach last_good_step, ie; index + steps[index] >= last_good_step.
That essentially means the current index can reach to a last_good_step that can eventually reach end.

Steps
-------
- Make last_good_step as len(arr) or N
- Iterate back from N-1 to 0, check the max steps ie; the nums[index] + index >= last_good_step (checking can be reachable)
- If Yes update last_good_step = index, else continue iteration to N-2, N-3 ... 0
- Atlast after all index iteration check last_good_step == 0, means index 0 can reach N.

"""

from typing import List


def canJumpBottomUpDP(nums:List[int]):
    n = len(nums) 
    dp = [False] * n 
    dp[-1] = True
    for index in range(n-2, -1, -1):
        for step in range(nums[index]+1):
            if index + step <= n-1 and dp[index + step]:
                dp[index] = True
                break
            dp[index] = False

    return dp[0] == True

def canJumpGreedy(nums:List[int]):
    last_good_step = len(nums) - 1
    n = len(nums) 
    for index in range(n-2, -1, -1):
        if index + nums[index] >= last_good_step:
            last_good_step = index
    return last_good_step == 0

print(canJumpBottomUpDP([2,3,1,1,4]))
print(canJumpBottomUpDP([3,2,1,0,4]))
print(canJumpBottomUpDP([3, 4, 2, 1, 2, 1, 5, 1, 0, 2, 1]))
print(canJumpGreedy([2,3,1,1,4]))
print(canJumpGreedy([3,2,1,0,4]))
print(canJumpGreedy([3, 4, 2, 1, 2, 1, 5, 1, 0, 2, 1]))
