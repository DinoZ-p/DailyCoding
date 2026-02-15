"""
Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
 
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 
Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        i = m-1
        j = n-1
        k = m+n-1
        while j >= 0:
            if i < 0:
                nums1[k] = nums2[j]
                j-=1
                k-=1
            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
                k-=1
            else:
                nums1[k] = nums2[j]
                j-=1
                k-=1
        return nums1
    
"""
idea: since len(num1)=m+n so there are space for num2 elements. The core idea is to adopt merge sort strategy.
we compare the largets number for num1 it is m-1, for num2 is n-1. and the space we left to put the numer is
last index which is len(num1)-1 which is also m+n-1

we use i to track elements in num1(rest are just bunch of 0s)
j to track elements to track num2 elements
k is the total len of num1

first if statement checks if num1 is empty then we just copy past nunm2 elements
elif is comparing largest element in num1 and num2 and replace with the 0
so does else

finnally return edited num1, not new list

"""