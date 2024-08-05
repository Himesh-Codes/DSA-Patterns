"""
Longest Repeating Character Replacement
Difficulty: Medium

https://leetcode.com/problems/longest-repeating-character-replacement/description/

You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing 
the above operations.


Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Solution (BruteForce)
----------------------
For each char in string, traverse from it's current posistion and go to the end of string, seeing that
if condition replacements are done is less than K. 
In traversal current element matches with starting element move index + 1, without reducing K.
Else reduce K and move index + 1, until K is 0.


Solution (Optimised)
----------------------
Sliding Window concept
https://www.youtube.com/watch?v=gqXU1UyA8pk

Intuition
---------
If we can create a window slides or grow to right for each char until it is valid.
How to know valid? : We have to see the most frequent element in window and take a count of elements.
Mismatch elements count in window can be calculated len(window) - most_frequent_char_count.
eg: If window is |B A B B A|, we have count[B] == 3, count[A] == 2,
mismatch count = 5 - count[B] = 5 - 3 = 2. Until this is valid with K (in our case K = 2), we can slide
the window to right.

If not valid? : Then we will take out left element and keep on increasing our right pointer until window
valid.
eg: |A B B A|, K=1
Now count[A] == 2, count[B] == 2, windwlen (4) - 2 = 2, since K is 1 we know current char made the window
not valid so to see the possibility, we will increse left+1 until window is valid.
And then only slide the window to right.

Steps
------
- maxFrequencyCount we keep to track most frequent char. (we will see the count if each element added and
parallely update maxFreq.)
So we see not decrement the maxFreq when left is increased or a char is removed from window.
Becuase maxFreq decreasing will not change our result, only increasing our maxFreq make change.
- count is hashmap for all elements in window.
- right - left + 1 will give len of window and max(count.values) will give maximum value of most freq
element in hashmap.
- Check window valid and slide to right until it is valid.
- If not valid reduce the left element count from hashmap and increase left += 1, and keep sliding right.

"""
class Solution:
    def characterReplacementOptimised(self, s: str, k: int) -> int:
        maxWindowSize = 0
        count = {}
        left = 0
        maxFreq = 0

        # increasing the right pointer until end
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFreq = max(maxFreq, count[s[right]])

            # check window valid if not pop out left most element from window
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            maxWindowSize = max(maxWindowSize, right - left + 1)

        return maxWindowSize
    
    def characterReplacement(self, s: str, k: int) -> int:
        maxWindowSize = 0
        count = {}
        left = 0

        # increasing the right pointer until end
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            # check window valid if not pop out left most element from window
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            maxWindowSize = max(maxWindowSize, right - left + 1)

        return maxWindowSize

# Testing
sol = Solution()
print(sol.characterReplacement("AABABBA", 1))
print(sol.characterReplacementOptimised("AABABBA", 1))
