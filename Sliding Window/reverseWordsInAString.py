"""
Reverse Words in a String

Difficulty: Medium

https://leetcode.com/problems/reverse-words-in-a-string/description/

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Solution (Brute Force)
----------
Convert the string into array of words and then reverse the array. Again convert array to a string.

Time = O(N + N) Space = O(N + N)

Steps
-------
- Construct words array from the string
- Traverse from right (end) to left (start) of the array and construct a new string with single whitespace after each word.

Solution (Optimised) - Sliding Window
----------
Do the sliding window from the end of the string and build a new string.
We can reduce the linear time and space complexity.

Time = O(N) Space = O(N)

Intuition
----------
While sliding window from end to start of string, we can identify each individual word and on the way construct a new string.

Steps
-------
- First check whether string is empty if yes return ""
- Place R & L until an alphabet found or not equal " " whitespace found.
- Start R and L pointers from end of string and identify each word, how?
- Pause the L pointer moving left once a whitespace found and that is a word to append to new string variable, with a trailing whitespace.
- Reset R & L with same technique in step 2.
- Add whitespace only if the L != 0, ie, first word in string found.

"""

def placeLeftNRightPointer(pointer:int, s: str):
    while not s[pointer].isalnum():
        pointer -= 1
    return pointer

def reverseWords(s: str) -> str:
    n = len(s)
    new_string = ""
    left = right = placeLeftNRightPointer(n-1, s)

    while left > -1 and right > -1:
        while s[left] != " " and left > -1:
            left -= 1
        if new_string != "":
            new_string += " " + s[left+1:right+1]
        else:
            new_string = s[left+1:right+1]
        left = right = placeLeftNRightPointer(left, s)
    
    return new_string

print(reverseWords("a good   example"))
