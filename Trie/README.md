# Trie

A Trie, also known as a prefix tree, is a specialized tree-like data structure used to store a dynamic set of strings where the keys are usually strings. It is particularly useful for applications that involve searching and prefix-based operations. Here are some key characteristics and common uses of a Trie:

### Characteristics of a Trie

- Nodes and Edges: Each node represents a character of the string, and the path from the root to a node represents a prefix of the stored strings.
- Root Node: The Trie starts with an empty root node.
- Children: Each node can have multiple children, typically stored in an array, a list, or a dictionary.
- End of Word Marker: A special marker (often a boolean flag) is used to indicate the end of a word.

### Common Operations

- Insertion: Adding a new word to the Trie.
- Search: Checking if a word exists in the Trie.
- Prefix Search: Finding all words that start with a given prefix.
- Deletion: Removing a word from the Trie (less common).

## Applications of Trie

- Autocomplete: Efficiently finding all words that start with a given prefix.
- Spell Checker: Quickly checking if a word exists in a dictionary.
- IP Routing: Used in networking to store routing tables for fast lookup.
- Longest Prefix Matching: Finding the longest prefix of a given string that exists in the Trie.
- Data Compression: Used in algorithms like LZW compression.
