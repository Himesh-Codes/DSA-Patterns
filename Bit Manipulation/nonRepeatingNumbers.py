"""
Non Repeating Numbers
Difficulty: Medium
https://www.geeksforgeeks.org/problems/finding-the-numbers0215/1

Given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs 
whereas the other two number occur exactly once and are distinct. Find the other two numbers. 
Return in increasing order.

Example 1:

Input: 
N = 2
arr[] = {1, 2, 3, 2, 1, 4}
Output:
3 4 
Explanation:
3 and 4 occur exactly once.
Example 2:

Input:
N = 1
arr[] = {2, 1, 3, 2}
Output:
1 3
Explanation:
1 3 occur exactly once.

Your Task:
You do not need to read or print anything. Your task is to complete the function singleNumber() 
which takes the array as input parameter and returns a list of two numbers which occur exactly 
once in the array. The list must be in ascending order.

Expected Time Complexity: O(N)
Expected Space Complexity: O(1)

Solution (XOR)
--------------

Binary Representation of an number:
13 ÷ 2 = 6 remainder 1
 6 ÷ 2 = 3 remainder 0
 3 ÷ 2 = 1 remainder 1
 1 ÷ 2 = 0 remainder 1

Reading the remainders from bottom to top, we get: 1101
So, 13 in decimal is 1101 in binary.

https://youtu.be/2D0D8HE6uak?t=1503

+

https://www.geeksforgeeks.org/find-two-non-repeating-elements-in-an-array-of-repeating-elements/

First, calculate the XOR of all the array elements. xor = arr[0]^arr[1]^arr[2]…..arr[n-1]

All the bits that are set in xor will be set in one non-repeating element (x or y) and not in others. 
So if we take any set bit of xor and divide the elements of the array in two sets one set of elements
with same bit set and another set with same bit not set. By doing so, we will get x in one set and y 
in another set. Now if we do XOR of all the elements in the first set, we will get the first non-repeating 
element, and by doing same in other sets we will get the second non-repeating element.

We have the array: [2, 4, 7, 9, 2, 4]

XOR = 2 ^ 4 ^ 7 ^ 9 ^ 2 ^ 4 = 2 ^ 2 ^ 4 ^ 4 ^ 7 ^ 9 = 0 ^ 0 ^ 7 ^ 9 = 7 ^ 9 = 14
The rightmost set bit in binary representation of 14 is at position 1 (from the right).
Divide the elements into two groups based on the rightmost set bit.
Group 1 (rightmost bit set at position 1): [2, 7, 2]
Group 2 (rightmost bit not set at position 1): [4, 9, 4]
XOR all elements in Group 1 to find one non-repeating element.
Non-repeating element 1 = 2 ^ 7 ^ 2 = 7
XOR all elements in Group 2 to find the other non-repeating element.
Non-repeating element 2 = 4 ^ 9 ^ 4 = 9
The two non-repeating elements are 7 and 9,

"""
class Solution:
    def singleNumber(self, nums):
        # Pass 1:
        # Get the XOR of the two numbers we need to find
        diff = 0
        for num in nums:
            diff ^= num

        # Get its last set bit
        diff &= -diff

        # Pass 2:
        rets = [0, 0]  # this list stores the two numbers we will return
        for num in nums:
            if (num & diff) == 0:  # the bit is not set
                rets[0] ^= num
            else:  # the bit is set
                rets[1] ^= num

        # Ensure the order of the returned numbers is consistent
        if rets[0] > rets[1]:
            rets[0], rets[1] = rets[1], rets[0]

        return rets

# Testing
sol = Solution()
print(sol.singleNumber([1, 2, 3, 2, 1, 4]))