"""
Docstring for leetcode.jumpGameII
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        i = 0
        farthest = 0
        count = 0
        while i < len(nums)-1:
            farthest = max(farthest, i + nums[i])
            if i == current:
                count+=1
                current = farthest
            i+=1
        return count
    
"""
the constrain for this problem than jump game one is that we should use the least jumps to reach end of the index
since we want to end of index, when the last index is reachable we do not need to jump again
so the loop here is len(nums)-1 instead of len(nums)

we still use greedy algorithm see what is the farthest we could reach from current end 
farthest = max(farthest, i + nums[i]) finds out the furthest we could reach, but we dont jump yet
when we reach i == to the current number that means it is out of limit and we have to jump 
so this time we update jump+1 and update the current location to the farthest we can reach. and increament i for loop
and eventually we will find out the total jump to reach the last index.

"""