"""
Docstring for leetcode.rotateArray
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution(object):
    def reverse(self, arr,left,right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums,0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        return nums
        
"""
question is asking us to roate k amount of numbers from back to front
the idea is that we can reverse the whole array so that the numbers we want to
put at the front is at the front already, just fix the order
then we can reverse each part seperately to fix the oder
after reverse, first part is 0 to k-1, we reverse these
after reverse, second part is k to n-1, we reverse these
after these operation, we foud out the exact way we want

k=k%n garentees that the number we get we will not roate over and over
for example is n = 5, k = 7. if we just throw k in there, after 5 times rotate, 
the array would back to same, so we are doing extra steps for it to back origin
after k%n, we can find out the actual useful steps of rotate.

for reverse, we could use build in reverse function. but here we define by ourself for 
better understanding
"""