"""
Median of Two Sorted Arrays
Difficulty: Hard

https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

Solution (BruteForce) - O(N)
----------------------
Merge 2 sorted array using 2 pointers concept in both of the array and get middle index by merge length.
If length is even take middle (index + 1) + index / 2 to get the median number. If odd length return the
middle index element.

Intutition / Observation
-------------------------
So in a merge array we will have a left partition and right partition for sure.
We will be calculating length of the total merging array, according to if it's odd or even, 
we can calculate the median.

For reduce the time complexity, we will be starting with the array with min length.

We have to find the mid1 and mid2, do recursive binary search on updating the mid1, mid2 accordingly.
eg: [2 8 9 15] , [1 3 4 7 10 12] => 1 2 3 4 7 | 8 9 10 12 15, median = 7 + 8 / 2 = 7.5

Dry run on above example
-------------------------

low = 0, high= 4, half = 4 + 6 // 2 = 5.
mid1 = low + high // 2 , mid2 = half - mid1
mid1 = 2, r2 = mid2 = 3
r1 = 2-1, r2 = 3-1 

2 8  | 9 15
1 3 4| 7 10 12

l1 = 8, r1= 9
l2= 4, r2= 7

l1 < r2 and l2 < r1
if out of bounds assign INT_MIN to l1 & l2
if out bounds assign INT_MAX to r1 & r2

if l1 > r2: high = mid1 - 1
else: low = mid1 + 1

mid1 = 0 + 1 //2 = 1, mid2 = 5 - 1 = 4
r1 = 1-1, r2 = 4-1

2   | 8 9 15
1 3 4 7 | 10 12

l1=2, r1=8
l2= 7, r2= 10

Now it is l1 < r2 and l2 < r1
return if even, total%2 == 0, max(l1,l2)
return if odd,  max(l1,l2) + min(r1, r2) / 2


Solution (Optimised) - O(log(m+n))
----------------------------------
https://www.youtube.com/watch?v=F9c7LpRZWVQ
https://www.youtube.com/watch?v=q6IEA26hvXc

Binary search on two sorted array.


"""