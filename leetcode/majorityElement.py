"""
Docstring for leetcode.majorityElement
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        count = 0
        i = 0
        while i < len(nums):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count +=1 
            else:
                count -= 1
            i+=1
        return candidate


"""
we could sort the nums first and find the n/2 number and that number is the majority. 
this approach needs O(1) space but need O(nlogn) time due to sorting

our approach is that scan each number to find the candidate. we set the first number as our candidate,
and compare with rest numbers. if we found next number is same, we add its count, if next number is not the same,
we decrese its count. untill when count reaches 0 that means current candidate have no chance
so we reassign the next number as our candidate and repeat.
when we scanned all numers we return the current candidate. the count could be 2, could 3, it is fine
to not match the exact count of that number in the list

this approach needs O(1) space and O(1) time. since it is just linear finding.

"""