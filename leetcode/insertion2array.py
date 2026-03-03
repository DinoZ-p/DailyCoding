"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common = set(nums1)
        ans = set()

        for num in nums2:
            if num in common:
                ans.add(num)

        return list(ans)

            
"""
hash map probelm. simplly add all numers into hash map, and run nums2, if we can find same number in hashmap.
that is a answer.

or can just do python build in funtion of two sets and print out the union of two set by using &
"""