"""
Docstring for leetcode.removeDuplicatedII
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 2
        k = 2
        while i < len(nums):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                i += 1
                k += 1
            else: 
                i+=1
        return k
        
        
"""
same thing for remove duplicated from sorted arrt, the array is sorted. we do not need to scan the 
elements in the array one by one.
question states that each number can apper up to 2 times. 
the idea is that we check every two numbers. for example if numer at index 0 is equal to 
numer at index 2, then the number at index 1 is definitly euqla to number at indx 0 and 2.
if they not euqal that means it is unique

i is to track the overal index which is the fast pointer
k is to track number appear mroe than 2 times which is the slow pointer 

at initiallize, if nums[i] != nums[k-2] we are comparing the first number and the third number in the list
if they are not equal that means it is unique. we assign the number to spot k. and increament both i and k
to move on

if they are the same, means it is not unique and appear more than two times, so we skip and move on to 
next index i.

eventaully return k

"""