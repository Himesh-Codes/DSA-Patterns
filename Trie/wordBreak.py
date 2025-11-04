"""
Word Break

Difficulty: Medium

https://leetcode.com/problems/word-break/description/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of 
one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

Solution (Brute Force)
----------
Try all the possible partitions of the given string and check if the left and right substrings are present in the dictionary.
Time complexity = O(2^N) Space = O(N) due to recursion stack.

Steps
-------
- Create a set of words from wordDict for O(1) lookup.
- Create a recursive function that takes the start index of the current substring.
- If start index reaches the end of the string, return True.
- For each possible end index from start+1 to len(s)+1, check if the substring s[start:end] is in the word set.
- If it is, recursively call the function with the new start index as end.

Solution (Optimised) : Trie + DP
----------

Time = O(N*L) Space = O(N + M)

Intuition
----------
We can mimik the same method we use in dictionary index (here Trie) to find the next word.
Like we start from the starting letter and then go to next letter and next to see a word exist in dictionary.

Steps
-------
Eg: s = "applepenapple", wordDict = ["apple", "pen"]

- building the Trie (node-by-node),
    root
    ├─ 'a' → a → p → p → l → e*   (* marks end_of_word)
    └─ 'p' → p → 'e' → n*         (this 'p' is different child at root from 'a' path)

- the DP array initialization, dp[0] = True (empty prefix), All others False initially.
    Index:   0 1 2 3 4 5 6 7 8 9 10 11 12 13
    s chars: a p p l e p e n a  p  p  l  e
    dp:      T F F F F F F F F F  F  F  F  F

- for each i where dp[i] == True, the inner Trie traversal (j increasing),
    i = 0 (dp[0] == True) — try to match words starting at s[0] = 'a'

    We traverse Trie along characters starting from index 0:

    j=0: char = 'a' → root has 'a' child → move to node 'a' (not end)
    j=1: char = 'p' → 'a' node → 'p' child → move (not end)
    j=2: char = 'p' → move (not end)
    j=3: char = 'l' → move (not end)
    j=4: char = 'e' → move → node is end_of_word for "apple"
    So at j=4 we found "apple" (s[0:5] == "apple"). Set dp[5] = True.

    dp indices: 0 1 2 3 4 5  6  7  8  9 10 11 12 13
    dp values:  T F F F F  T  F  F  F  F  F  F  F  F
                ^                     (dp[5]=True set)
    
    i = 1..4 (dp[1..4] are False) — skipped
    No traversal because dp[1..4] are False (prefixes "a", "ap", "app", "appl" are not fully segmentable).

    i = 5 (dp[5] == True) — try to match words starting at s[5] = 'p'

    Now traverse from index 5:
    j=5: char = 'p' → root has 'p' child (start of "pen") → move
    j=6: char = 'e' → move
    j=7: char = 'n' → move → node end_of_word for "pen"
    At j=7 we found "pen" (s[5:8] == "pen"). Set dp[8] = True.


- all dp updates and final result.

    dp[n] = dp[13] = True → s can be segmented as "apple" + "pen" + "apple" → return True.
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode() #root of the Trie
    
    def insertIntoTrie(self, word):
        node = self.root

        for char in word:
            node = node.children.setdefault(char, TrieNode()) #if exists we get exist child node
        node.isEndOfWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        trie = Trie()

        for word in wordDict:
            trie.insertIntoTrie(word)
        
        dp = [False] * (n + 1)
        dp[0] = True
        index = 0

        while index < n:
            if not dp[index]:
                index += 1
                continue 

            node = trie.root
            for segmentIndex in range(index, n):
                char = s[segmentIndex]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.isEndOfWord:
                    dp[segmentIndex + 1] = True
                    if dp[n]: return True #early exit reduce linear complexity
            index += 1
        
        return dp[n]

sol = Solution()
# print(sol.wordBreak("applepenapple", ["apple", "pen"]))
# print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
print(sol.wordBreak("aaaaaaa", ["aaaa","aaa"]))
