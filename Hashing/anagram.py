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


"""
MAKE ANAGRAM

`Difficulty: Medium`

Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

Example
S= 'abccde'

Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

Function Description

Complete the anagram function in the editor below.

anagram has the following parameter(s):

string s: a string
Returns

int: the minimum number of characters to change or -1.

Input Format

The first line will contain an integer, , the number of test cases.
Each test case will contain a string .

Input1:
S = "aabbkbaytl"

str1 = "aabbk" str2= "baytl"

Input1:
S = "aaababbb"

str1 = "aaab" str2= "abbb"

Solution
-------------------------
Split string S into str1 and str2. 
Use two hashmaps log the chars count in corresponding hashmap.
iterate through each hashmap and find the difference in common strings and uncommon string

Trick here is anyway if we found the difference with common strings in one way let's say hashmap1 to hashmap2, it will be same vice versa.
But in extra the uncommon string should be calculate in reverse hashmap2 -> hashmap 1 since that is also a difference.
And take the half of total difference since the changes are reflecting in both strings, we only need half of change

eg: `aaab` is having common string difference 2 (A's). `abbb` have common string difference of 2 (B's), so 2+2 / 2 = 2 is the answer.

Edge cases
---------------
1) If string len not even then return false, since it can't be equally splitted
2) On the comparison of 2 hashmaps check conditions
    a) If Char not found in other hashmap increase difference by it's count
    b) If found char then add the difference of it's count in other hashmap
    c) traverse and add the uncommon string count in hashmap2 also added in difference.
    c) take the half of total difference since total difference is calculated based on both strings difference. 
    If one string1 changed with other string2 char we don't need to change in string2 to string 1.

"""

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s)//2

    strOne = s[:mid]
    strTwo = s[mid:]

    # 
    strOneChars = {}
    strTwoChars = {}
    index = 0

    while index < len(strOne):
        if strOne[index] in strOneChars:
            strOneChars[strOne[index]] += 1
        else:
            strOneChars[strOne[index]] = 1

        if strTwo[index] in strTwoChars:
            strTwoChars[strTwo[index]] += 1
        else:
            strTwoChars[strTwo[index]] = 1

        index += 1

    difference = 0    
    # iterate through hashmap of str1 
    for char, count in strOneChars.items():
        if char not in strTwoChars:
            difference += count
        else:
            difference += abs(count-strTwoChars[char])
    
    # iterate through hashmap of str2 to find and add uncommon strings 
    for char, count in strTwoChars.items():
        if char not in strOneChars:
            difference += count
    
    return difference//2



print(anagram('abccde'))
print(anagram('aaababbb'))
