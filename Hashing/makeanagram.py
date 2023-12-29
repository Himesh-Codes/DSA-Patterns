
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

