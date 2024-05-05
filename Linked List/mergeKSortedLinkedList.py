"""
Merge k Sorted Lists
Difficulty: Hard
https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

Solution 1
------------
We can use the K pointers in hashmap, and add iterating pointers. (Space complexity O(K))
Also we will have to initiate the pointers in hashmap with all linkedlist head. (Complexity O(K))
And iterate every linkedlist toghether in a loop until the longest length list is covered, 
and compare everytime which node is smaller and assign to our dummy list. (Complexity O(N)).
Also the dummy list space will be O(M).

Time Complexity: O(N)
Space complexity: O(K + M)

Solution (Optmised)
---------------------
Use of the divide and conquer method, merge sort algorithm in lists and merge the sorted linked lists.
Since the linkedlists are sorted alrady we don't want to sort the list

Merge Lists (Iterative)
------------------------
Run thorough the list of the linkedlist in O(N) complexity
And merge the linkedlists iteratively in with inserting the nodes. Until the lists node are completely traversed.
Here the lists are merged so the no space are used space complexity is the O(1) 

Min-Heap for optmised solution
----------------------------
Gives you the minimum value, using a priority queue.
Storing the pair of integer and node as the values.
Use heapq in python (basically create a min-heap, ie, tree with root node have small value)
heapq.heappush is O(logN), also heapq.pop will be same O(logN)
heapq.heapify is O(N), basically construct a tree


Steps
---------
1) Add the head nodes to priorityQueue. In format pair(integerValue, node). Complexity O(N)
2) Do heapq.heappop to give us the min value pair (integerValue, node), in an array/set.
3) Once pop, try add that pop node.next into queue, until value of linkedlist node is NULL. 
Add pop element Complexity O(logN) into our dummyNode list.
4) While until priorityQueue is empty do 2-3 steps iteratively, return generated list.

Time Complexity: O(NlogN + K) => O(K log N)
Space Complexity: O(K), K is max size of priority queue.
"""
import heapq
from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      priorityQueue = []
      hashmap = {}

      for index, list in enumerate(lists):
        if list:
          hashmap[index] = list
          heapq.heappush(priorityQueue, (list.val, index))
      
      dummyNode = ListNode(-1)
      current = dummyNode
      while len(priorityQueue) > 0:
          value, index = heapq.heappop(priorityQueue)
          current.next = hashmap[index]
          current = current.next
          if hashmap[index].next:
            print(hashmap[index].next)
            heapq.heappush(priorityQueue, (hashmap[index].next.val, index))
            hashmap[index] = hashmap[index].next

      return dummyNode.next
    

# Testing

sol = Solution()
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list3 = ListNode(2)
list3.next = ListNode(6)
res = sol.mergeKLists([list1, list2, list3])
while res:
  print(res.val, "->")
  res = res.next
