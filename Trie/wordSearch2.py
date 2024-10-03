"""
Word Search II
Difficulty: Hard
https://leetcode.com/problems/word-search-ii/description/

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Solution (Bruteforce)
---------------------
We do DFS on each and every position and bruteforce and see the word forms are in set.
If found put into result.
Time Complexity: O(N3)

Intuition
-----------
To optimise the search with DFS, we need to get a data structure which can be search with prefix of a
word in every position: We use TRIE (aka Prefix Tree).


https://www.youtube.com/watch?v=asbcE9mZz_U
Solution (Trie)
------------
trick: I though use trie to store the grid, reverse thinking, instead store dictionary words, 
dfs on each cell, check if cell's char exists as child of root node in trie, if it does, update currNode, 
and check neighbors, a word could exist multiple times in grid, so don't add duplicates;

Build a Prefix tree like below for checking words:
Because rather than create a trie for board and check each word exist the reverse logic works more better.
eg:[[a,c][p,e]]

[a  c
 p  e]      words = [ape, app, ace]

        root
        /
        a
      /   \
    c       p
   /       / \
   e       p    e

Now while doing a DFS from board and recurse thorugh all possible out we can see the words are made.
And if a prefix not exist we can say the DFS recursion not at all needed.

Time Complexity: O(N*M*K)
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False
    
    def addWord(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWordEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows , cols = len(board), len(board[0])
        result , visit = set(), set()

        # node for what node visited in previous DFS on trie
        # word : what word formed so far
        def dfs(r, c, node: TrieNode, word):
            # If the current DFS char is not in node children that means DFS is not need further
            if (r<0 or c<0 or r==rows or c==cols or (r,c) in visit) or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWordEnd:
                result.add(word)
            
            # four directions traversal
            dfs(r-1,c,node, word)
            dfs(r+1,c,node, word)
            dfs(r,c-1,node, word)
            dfs(r,c+1,node, word)

            # remove the visited node once before bactracking after all it's child DFS done
            visit.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root, "")
        
        return list(result)

# Testing
sol = Solution()
print(sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))