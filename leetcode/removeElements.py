"""
Docstring for DailyCoding.leetcode.removeElements
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                i +=1
            else:
                nums[k] = nums[i]
                i +=1
                k +=1
        return k
"""
the question is asking to skip elements that == to the val, and keep elements != val and return k
the idea is that we use i to keep track the overall index for nums, k to track the none euqal elements in nums

i times loop to scan every elements in nums. 
if we find nums[i] == val, that means we do not want
it so we skip it and move on. Note here k is not changed, which means this is the spot where we want
to replace with the value != val
if the ith numer is != val, then we know this is the numer we want to keep, we will assign it at where the 
numer we do not want which is at nums[k]. we increament k so that we know this spot has been taken by valid 
numbe so we move on. i is always increamenting since it is scanning the whole array.

reason why we do not use pop() here is that in the question it says algo needs to be in-place
pop() is in-place operation but it take O(n) time, for worest case it takes O(n^2)
in place means no extra copy, array, space created. and often requires O(1)
another reason why we dont use pop() is becuase pop() will automatically shift numers to left side
leading diffulc to track the index so might skip number.

"""