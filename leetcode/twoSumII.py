"""

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        cur_sum = 0
        while left < right:
            cur_sum = numbers[left]+numbers[right]
            if cur_sum > target:
                right -=1
            elif cur_sum < target:
                left +=1
            else:
                return [left + 1, right + 1]
            

"""
the array is sorted so we can use two pointers to find the target sum.
we can initialize one pointer at the beginning of the array and another pointer at the end of the array.
then we can calculate the sum of the two numbers at the pointers. 
if the sum is greater than the target, we can move the right pointer to the left to decrease the sum.
if the sum is less than the target, we can move the left pointer to the right to increase the sum.
if the sum is equal to the target, we can return the indices of the two numbers.

note that the problem states that the array is 1-indexed, so we need to add 1 to the indices before returning them.

"""