"""
Docstring for leetcode.jumpGame
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        farthest = 0
        while i < len(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
            i += 1
            
"""
The idea here is to use greedy algorithm
i is to track the index of the array
farthest is the farthest index each step can reach
if i is > farthest index then that means the first number is 0, we cannot reach anything from there
BUT, we can reach itself which is also 0 
for [0], we will get through to farthest which is 0 and check >= len(nums) -1 which in this case is 1-1=0
it satisfy so we return True

we use farthest = max(farthest, i + nums[i]) to find out the furthest index the jump could reach 
nums[i] is the max jump we can do and since we doing greedy algoithm so we maximize it
keep doing the loop untill we can reach the last index number
"""
