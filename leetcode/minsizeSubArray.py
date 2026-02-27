"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        window_sum = 0
        best = len(nums)+1

        for right in range (len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                best = min(best, right - left + 1)
                window_sum -= nums[left]
                left += 1
        if best == len(nums)+1:
            return 0
        else:
            return best
        
        
"""
this is a sliding window problem. we can use two pointers to represent 
the left and right boundaries of the window.
we can initialize the left pointer at the beginning of the array and the right pointer at the beginning of the array as well.
then we can move the right pointer to the right and keep adding the numbers to the window sum until 
the window sum is greater than or equal to the target.

when the window sum is greater than or equal to the target, 
we can update the best length of the subarray and move the left pointer to the right to try to 
find a smaller subarray that still satisfies the condition.

if we reach the end of the array and the best length is still len(nums)+1,
it means that there is no such subarray, so we can return 0.
otherwise, we can return the best length of the subarray.

"""