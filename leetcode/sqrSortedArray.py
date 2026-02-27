"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        right = n - 1
        res = [0] * n
        pos = n - 1
        while left<=right:
            if abs(num[left] > abs(nums[right])):
                res[pos] = nums[left] * nums[left]
                left += 1
            else:
                res[pos] = nums[right]*nums[right]
                right -=1
            pos -=1
        return res
    
"""
it is very easy to do in brute force way, we can just square each element and sort the new array.

the O(n) way is to use two pointers, one pointer at the beginning of the array 
and another pointer at the end of the array.
we can compare the absolute value of the numbers at the two pointers, and square the larger one
and add it to the result array from the end to the beginning.
then we can move the pointer of the larger absolute value to the next position 
and repeat the process until the two pointers meet.

this way the time complexity is O(n) because we are only iterating through the array once.
and the space complexity is O(n) because we are using a new array to store the result.

"""