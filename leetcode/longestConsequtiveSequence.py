"""

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + 1 in num_set:
                    num += 1
                    length += 1
                longest = max(length, longest)
        return longest
"""
since the question ask us in O(n) so we cannot use sort
what operation is only O(1) is hashtable again

so store every number into the hashtable.

if a buch of numbers are consequtive, then they satisfy the next number is definitly n+1 and so on.
for the loop check, since we want the number start as the lowest, so we do if num - 1 not in num_set
so for example like num now is 4, and num-1 = 3. and 3 is in the hashtable, so if we start as 4, that will not be longest
becuase we missed a 3 or potentially 2 and so on.
afer we find that there are number +1 in the hashtable we update the number to number +1 also the lenth, untill we find a num+1 is not in table then that is the longest length
"""
