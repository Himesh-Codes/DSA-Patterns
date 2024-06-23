"""
Merge Sort
Difficulty: Medium
https://leetcode.com/problems/sort-an-array/description/

Solution (Divide & Conquer/ Merge Sort)
---------------------------------------
1) Divide the array into two equal halfs, leftarray and rightarray.
2) Base case of recursion is return array if len(arr) is 1.
3) Then from return value of left and right array, use 3 pointers (left, right, current).
4) LEFT pointer at left array index and RIGHT pointer at right array index, CURRENT pointer at main array. 
5) Compare each other and replace the currentIndex value in main array with least found value.
6) The end recursion values of left and right array will be always sorted.
7) So it's a matter of compare and increase index accordingly and place elements.
8) The leftover elements in left / right array after comparision should be added at end.
Either one array may have elements.


Time Complexity: O(NlogN)
"""
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums: List[int]):
            if len(nums) == 1:
                return nums
            mid = len(nums)//2
            leftArray = mergeSort(nums[:mid])
            rightArray = mergeSort(nums[mid:])

            left = right = current = 0
            while left < len(leftArray) and right < len(rightArray):
                if leftArray[left] < rightArray[right]:
                    nums[current] = leftArray[left]
                    left+= 1
                else:
                    nums[current] = rightArray[right]
                    right+= 1
                current+= 1

            while left < len(leftArray):
                nums[current] = leftArray[left]
                left+= 1
                current+= 1
            while right < len(rightArray):
                nums[current] = rightArray[right]
                right+= 1
                current+= 1

            return nums

        return mergeSort(nums)

# Tesing
sol = Solution()
print(sol.sortArray([-2, -4, 7, 0, 180, 45, 87, 51, 3, 17]))