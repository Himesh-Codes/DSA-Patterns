"""
Difficulty: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Solution
 ------------
    Use a hashmap to enter the string one chars, keep count 1, string 2 increase char count, in corresponding hashmaps
    Since we iterate parallelly on string for optimisation we increase the count gradually in corresponding hashmaps.

    Then iterate hashmaps if any chars on same two hashmap same it is anagram else not.

 Edge Cases
 ------------
 1) If len of each string is not same or If second string is empty return false
 2) If str2 map item not in str1 map , then return false
 3) If str2 map item count not equal str1 map, return false

 Note:
  We can't iterate toghether since the edge cases like str1 ="aa" str2="bb" fails with single hashmap.
  Or else we need two hashmaps that logs str1 and str2 seperately 

   https://leetcode.com/problems/valid-anagram/
"""

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    charCountStrOne, charCountStrTwo = {}, {}
    index = 0

    # traverse string toghether
    while index < len(s):
        if s[index] in charCountStrOne:
            charCountStrOne[s[index]] += 1
        else:
            charCountStrOne[s[index]] = 1

        if t[index] in charCountStrTwo:
            charCountStrTwo[t[index]] += 1
        else:
            charCountStrTwo[t[index]] = 1

        index += 1

    for char in charCountStrTwo:
        if char not in charCountStrOne:
            return False
        if charCountStrOne[char] != charCountStrTwo[char]:
            return False
    return True

print(isAnagram("anagram", "nagaram"))

print(isAnagram("rat", "car"))
print(isAnagram("aa", "bb"))
