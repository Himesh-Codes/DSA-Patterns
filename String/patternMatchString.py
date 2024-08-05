"""
Find the Index of the First Occurrence in a String
Difficulty: Easy/Medium
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.


Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 



Solution (Optimised)
---------------------
KMP algorithm , O(M+N)

Better Explaination
---------------------
https://www.youtube.com/watch?v=ziteu2FpYsA

Neetcode: https://www.youtube.com/watch?v=JoF0Z7nVSrA&t=919s

Time complexity: O(M+N)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle and len(needle) > len(haystack):
            return -1
        lps = self.findLPS(needle)
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            if j == len(needle):
                return i - len(needle)
        return -1
            

    def findLPS(self, p: str):
        lps = [0] * len(p)
        previousLPS, i = 0, 1
    
        while i < len(p):
            if p[i] == p[previousLPS]:
                lps[i] = previousLPS + 1
                previousLPS += 1
                i += 1
            elif previousLPS == 0:
                lps[i] = 0
                i += 1
            else:
                previousLPS = lps[previousLPS-1]

        return lps

 
    
# Testing
sol = Solution()
print(sol.strStr("sadbutsad", "sad"))
print(sol.strStr("AAAXAAAX", "AAAA"))