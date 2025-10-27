"""
Quick Sort

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: [2,3,5,7,9,10,18,101]

Example 2:

Input: nums = [0,1,0,3,2,3,0]
Output: [0,0,0,1,2,3,3]

Solution
---------
Using the logic divide and conquer by place the pivot element in middle, then split into left and right half arrays.
Again do same operation.

Time = O(NlogN) Space = O(logN) recursive stack

Steps
--------
QUICKSORT(A, low, high):
    if low < high:
        p = PARTITION(A, low, high)
        QUICKSORT(A, low, p-1)
        QUICKSORT(A, p+1, high)

PARTITION(A, low, high):   // pivot = A[high]
    pivot = A[high]
    i = low - 1
    for j from low to high-1:
        if A[j] <= pivot:
            i = i + 1
            swap A[i] and A[j]
    swap A[i+1] and A[high]
    return i + 1

- Find pivot (last element of array)
- Place pivot in middle, where left part of array elements are less than PIVOT and right elements greater
- Now we understand PIVOT is placed in correct poisition in array
- After iteration return the index of pivot
- Iteratively do above steps on each partition left and right
"""

from typing import List


class Solution:
    def quicksort(self, nums: List[int]) -> List[int]:
        def sortlist(nums, low, high):
            if low < high:
                partition_point = partition(nums, low, high)
                sortlist(nums, low, partition_point-1)
                sortlist(nums, partition_point+1, high)
        
        def partition(nums, low, high):
            pivot = nums[high]
            place_index = low - 1
            iteration_index = low
            while iteration_index < high:
                if nums[iteration_index] <= pivot:
                    place_index += 1
                    nums[iteration_index], nums[place_index] = nums[place_index], nums[iteration_index]
                iteration_index += 1
            nums[place_index+1], nums[high] = nums[high], nums[place_index+1]

            return place_index + 1
        
        sortlist(nums, 0, len(nums)-1)

        return nums

# Testing
sol = Solution()
print(sol.quicksort([3, 1, 5, 2, 4]))
print(sol.quicksort([0,1,0,3,2,3,0]))
print(sol.quicksort([10,9,2,5,3,7,101,18]))