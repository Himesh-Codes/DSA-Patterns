"""
Longest Palindromic Substring
Difficulty: Medium
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

Solution (1D DP)
-----------------
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
- Store the curLength (right-left+1), always in every spread loop.
- Compare with maxLength and update, if greater then update longestPalString with current string str[left: right+1].

Time Complexity: O(N2), since traversal of the each string index is O(N), and each time it spread wide O(N)
Space Complecity: O(N)

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalString = ""
        maxLength = 0

        def spreadCheck(left, right, maxLen, palString):
            curLength = 0
            
            # check out of bounds and left and right equal
            while left >= 0 and (right < len(s)) and (s[left] == s[right]):
                # check the length of current str
                curLength = right - left + 1 
                if curLength > maxLen:
                    maxLen = curLength
                    palString = s[left: right+1]
                left -= 1
                right += 1

            return [palString, maxLen]
        
        for index in range(0, len(s)):
            # odd palindrome
            longestPalString, maxLength = spreadCheck(index, index, maxLength, longestPalString)

            # even palindrome
            longestPalString, maxLength = spreadCheck(index, index+1, maxLength, longestPalString)

        return longestPalString

# Testing
sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("babbad"))
print(sol.longestPalindrome("ccc"))