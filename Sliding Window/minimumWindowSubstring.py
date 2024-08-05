"""
Minimum Window Substring
Difficulty: Hard
https://leetcode.com/problems/minimum-window-substring/description/

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 
https://www.youtube.com/watch?v=jSto0O4AJbM

Solution (Sliding window)
---------------------------
We use the left and right pointer sliding window with 2 hashmaps
1: windowHashmap: stores the count of matching char in matchHashmap for current window.
2: matchHashmap: which stores the count of chars in t string that need to match.

Inorder to reduce linear complexity of find matchHashmap and windowHashmap have element count matching
or windowHashmap[elem] >= matchHashmap[elem], for each element to add the minimum len string into result.

We use HAVE is a count of element satisfied windowHashmap[elem] == matchHashmap[elem]
Also NEED is count of element in string t.

We increase HAVE + 1 when we see windowHashmap[elem] == matchHashmap[elem].
And decrease HAVE - 1 if indowHashmap[elem] < matchHashmap[elem], when we move our left pointer on sliding.

We increase left until we minus one windowHashmap[element] -= 1.
And then increase right until the HAVE == NEED.

Keep a minLen variable to compare.
Whenever HAVE == NEED, we push the len of current window like right - left + 1 and see if it's minimum,
if minimum then push into result.

Also our aim to move left until we minus one windowHashmap[element] -= 1, we can reduce this iteration 
linear complexity by adding index of matching index into a queue. So if we got a result then slide window by
poping out queue and move to current first index in queue.

Eg:
Input: s = "ADOBECODEBANC", t = "ABC"
Here we will get the first result on window |ADOBEC|, and minLen = 6 now.
But when we pop out A to slide window from left + 1, we see next element is match "B" in index 3.
So if we have a queue, once pop A we pop leftmost in queue, and make left == queue[0], as index 
we can compare from there until other match came.

Note: We add into queue for all matching element index.
"""