"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i, val in enumerate(nums):
            if val in seen and abs(i - seen[val]) <= k:
                return True
            seen[val] = i
        return False
"""
we need to use hashmap to store the key and value(index)
for i and value in the list, we add the number as key and the index as its value

and if we found a numer in the hashmap then that means it is the duplicate number so we will use current i - its value(index)
and find abs value of it. if it is <= k that return true
else wise return false
"""


