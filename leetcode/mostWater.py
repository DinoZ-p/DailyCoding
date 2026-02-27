"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxwater = 0
        while left < right:
            water = min(height[left], height[right])*(right-left)
            maxwater = max(maxwater, water)
            if height[right] > height[left]:
                left +=1
            else:
                right -=1
        return maxwater
    
"""
even tho the list is not sorted, we can still use two pointers to find the maximum area of water.
we can initialize one pointer at the beginning of the list and another pointer at the end of the list.
then we can calculate the area of water between the two pointers.

the core is that lowest height decides the max height of the water, 
and the distance between the two pointers decides the width of the water.

so we use two pointers to find the max height and hope it is the max area.
if the height at the right pointer is greater than the height at the left pointer,

"""