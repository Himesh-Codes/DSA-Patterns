"""
 Search a 2D Matrix
 https://leetcode.com/problems/search-a-2d-matrix/description/
 Difficulty: Medium

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Examples
---------
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Intuition
----------
Binary search first on row range then inside a row.
Since array is monotonically increasing in row wise and inside a row. 
We can find target belongs to which row, by seeing target in between mid leftmost mid[0] and 
mid rightmost, mid[len(arr[mid])-1]. If found a range then return row index.

Now if we do binary search on the row index we found.

Time Complexity: O(log(m*n))

Solution
-----------
Use the binary search in rowwise range, and then on specific row. Since we can see the array is monotonically increasing.
Sorted array search commonly use binary search.

Steps
-----------
Example - Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
1) Consider pointers rangeleft and rangeright, rangeright at last row, in above example it is 4.
2) Find the mid for rangeleft pointer and see target in the range of mid point(l+r/2) array. Here we check 13 is in between
our first mid 1, so arr[1][0] <= target <= arr[1][4], check target contained in range, here yes.
3) So once we find the possibility of a target in a range then use that array for next binary search of target.
Here we use arr[1], ie target should be in range 10 - 20. So mid value is assigned to rangeleft.
4) Now use new left and right pointers, find mid = right+left/2, rangeLeft will be same, 
so we check arr[rangeLeft][mid] is less or greater or equal to target.
5) If less use mid-1 as right, if greater use mid+1 as left, if equal return True.
6) Do recursion until the left <= right.
7) If couldn't find return false.

Edge cases
------------
1)If len(arr) is 0, we return false.

"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRowRange(rangeLeft, rangeRight, target):
            if rangeLeft<= rangeRight:
                mid = (rangeRight + rangeLeft) // 2
                if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid])-1]:
                    return mid
                elif matrix[mid][0] > target:
                    return findRowRange(rangeLeft, mid-1, target)
                elif matrix[mid][0] < target:
                    return findRowRange(mid+1, rangeRight, target)
            return -1
        
        def findTarget(left, right, row, target):
            if left <= right:
                mid = (left + right) // 2
                if target == matrix[row][mid]:
                    return True
                elif target > matrix[row][mid]:
                    return findTarget(mid+1, right, row, target)
                elif target < matrix[row][mid]:
                    return findTarget(left, mid-1, row, target)
            return False

        row = findRowRange(0, len(matrix)-1, target)
      
        if row == -1:
            return False
        return findTarget(0, len(matrix[row])-1, row, target)
        

# Testing
sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(sol.searchMatrix([[1],[3]], 2))