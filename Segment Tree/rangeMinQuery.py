"""
Range Minimum Query
Difficulty: Medium
https://www.geeksforgeeks.org/problems/range-minimum-query/1

Given an array A[ ] and its size N your task is to complete two functions  a constructST  
function which builds the segment tree  and a function RMQ which finds range minimum query in a 
range [a,b] of the given array.

Input:
The task is to complete two functions constructST and RMQ.
The constructST function builds the segment tree and takes two arguments the array A[ ] and 
the size of the array N.
It returns a pointer to the first element of the segment tree array.
The RMQ function takes 4 arguments the first being the segment tree st constructed, second being 
the size N and then third and forth arguments are the range of query a and b. 
The function RMQ returns the min of the elements in the array from index range a and b. 
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function RMQ should return the min element in the array from range a to b.

Example:

Input (To be used only for expected output) 
1
4
1 2 3 4
2
0 2 2 3

Output
1 3

Explanation
1. For query 1 ie 0 2 the element in this range are 1 2 3 
   and the min element is 1. 
2. For query 2 ie 2 3 the element in this range are 3 4 
   and the min element is 3.

Solution (Segment Tree)
------------------------
Segment tree will create the tree from array in time complexity O(N)
And use a space of O(N)
And give the minimum number in O(logN)
When we deal will lot of data in array the Native approach won't be scalable.

https://www.youtube.com/watch?v=ZBHKZF5w4YU

Segment Tree
------------
Eg: [-1, 2, 4, 0]
It will be look like :


                    -1 [0,3]
                /          \
              -1 [0,1]       0 [2,3]
            /   \           /    \
    [0,0] -1    [1,1] 2 [2,2] 4    0[3,3]


We split the array into half until we got each single element and on bactrack create a 
tree with leaf nodes be the array element and parent nodes will be the min of leaf nodes.
And so on to root we do same.

Now on above tree we while finding min we have 3 possibility:
eg : range = [1,3]

1) partial overlap : if the range of a node is partial overlap with range go to left and right child.
eg: root [0,3] go to left and right see until fully overlap.

2) fully overlap: if fully overlap then return the node value.
eg: [1,1] is fully overlap by [1,3], so return 2 from node.

3) not overlap: if not overlap we return MAX (float("inf")) value.
eg: [0,0] not overlap so return MAX

On every node on backtrack we see what is min(left, right) return values then that is passed to parent on
backtrack.
Atlast in root we will get what is min.
"""