"""
LRU Cache
Difficulty: Medium

https://leetcode.com/problems/lru-cache/description/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. 

Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Solution (Brute Force)
----------
Brute Force: Using a list/stack as a cache to store key and dictionary store key-value pairs

Time = O(N) for get & O(N) for put, Space = O(N)

Steps
-------
Get: Search key in dict, if found search key in array, pop() from current pos and add in the end of array to mark recent usage.
Put: Update the key with current value if exists, else create entry in dict and in array/stack append key to end.
If capacity exceeds we have to evict the first item in array that is LRU pop(0) and remove from dict


Solution (Optimised Doubly LinkedList)
----------
Using a doubly linked list to track the least / most recently used item.

Time = O(1) for get & O(1) for put, Space = O(N)

Intuition
--------------
Using the doubly linked list we can get an element data and move it to front or back of the linkedlist.
Hashmap contains details with key-node pair, node will contain key, value, next, previous data.
We have to keep a dummy head and tail details of the linkedlist which will help to identify most recent and least recent used.

Steps
-------
Get: Search key in dict, if found search key in array, remove node from the current pos and add to start of the linkedlist.
Put: Update the key with current value if exists, remove node and add to start of linkedlist, 
else create entry in dict and a new node append to start of list.
If capacity exceeds we have to evict the last item with refer to tail in linkedlist and remove from dict.

"""
class Node:
    def __init__(self, key:int, value: int):
        self.value = value
        self.key = key
        self.next = None
        self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node: Node = self.cache[key]
        self.remove(node)
        self.insertToHead(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insertToHead(node)

        if len(self.cache) > self.capacity:
            lruItem: Node = self.tail.previous
            self.remove(lruItem)
            del self.cache[lruItem.key]

    
    def insertToHead(self, node:Node):
        head, nextToHead = self.head, self.head.next
        node.previous, node.next = head, nextToHead
        head.next = nextToHead.previous = node

    def remove(self, node:Node):
        previousNode, nextNode = node.previous, node.next
        previousNode.next, nextNode.previous = nextNode, previousNode
        

lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))   # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))   # return 3
print(lRUCache.get(4))  # return 4