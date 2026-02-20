"""
Docstring for leetcode.productOfarrayExceptItself
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        prefix = 1
        answer = [1] * n
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
    
"""
constain here is to keep it O(n), if we want to bruteforce to compute, we could slices them and use nested loop *=
but that will take O(n^2)

here the idea is that we first define the answer list with bunch of 1's, since multiplying 1 doesnt affect anything
and then we first compute the left part of that number with respect of setiing prefix = 1 to start.
and the number i will be the current index that we currently filling, so we are updating it and do not multiply it

after we get all the numbers that are computed by left. we use the answer we alredy got to multiply with right side
untill run out of all numbers and return the answer[]. this guarentee O(n)
"""