"""
Palindromic Substrings
Difficulty: Medium
https://leetcode.com/problems/palindromic-substrings/description/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

Solution (Brute Force) - Time Complexity: O(N3)
-----------------------
Taking each and every char in a string and create substrings from start left to end right ( it is O(N2)), 
and determine whether developed substring is a palindrome (it is O(N)).

Solution (1D DP)(Optimised) - Time Complexity: O(N2)
----------------------------
- Spread wide concept.
- Considering each index in string array as the starting point and spread equally to left and right and see the possibility of palindromes.
- Two cases of checking in each index, 
    checking "odd palindromes" consider center at one index (i), 
    checking "even palindromes" consider center at two adjacent index (i, i+1).
eg: "babbad"
We start will index(0), "b", having no left, then check even palindrome "b" "a" not equals
Next start will index(1), "a", having left "b", right "b", len of palindrome is 3 so update with maxLenght and palidromeStr,
then check even palindrome "a" "b" not equals
This continues until and index are traversed and spreadout.

Steps
--------
- Loop run on the each index string.
- Do spread wide operations in index, left-1 and right+1, until break conditions (str[left] == str[right]) or outofbounds met
    - "odd palindrome spread" - check until out of bounds and left, right = index first, then iterate using spread left -= 1, right += 1
    - "even palindrome spread" - check until out of bounds and left = index, right = index +1 first, then iterate using spread left -= 1, right += 1
- Update palindromeCount +1 everytime when we find a substring that is palindrome.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        def spreadCheck(left, right):
            palindromeCount = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindromeCount += 1
                left -= 1
                right += 1
            return palindromeCount

        for index in range(len(s)):
            palindromes+= spreadCheck(index, index)
            palindromes+= spreadCheck(index, index+1)
        return palindromes

# Testing
sol = Solution()
print(sol.countSubstrings("abc"))
print(sol.countSubstrings("aaa"))