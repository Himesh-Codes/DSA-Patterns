"""
Difficulty: Easy

https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

Solution
-----------
Use the two pointers left and right (as len-1), then iterate in string toghether. And check if string chars in the positions are not same.
The return false, else everything match until end of iteration return true.

Complexity - O(N)

Edge cases
-----------
1) create an array of char filter the alphanumeric only and eliminates special charr- O(N)

"""

def isPalindrome(s: str) -> bool:
    # list comprehension to filter special char and contain alphanum only
    charArrayFiltered = [char for char in s if char.isalnum()]

    left = 0
    right = len(charArrayFiltered) - 1

    while left < right:
        if charArrayFiltered[left].lower() != charArrayFiltered[right].lower():
            return False
        left += 1
        right -= 1

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))