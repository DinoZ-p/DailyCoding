"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solution = []
        n = len(nums)
        for fixed in range(0, n-2):
            if fixed > 0 and nums[fixed] == nums[fixed-1]:
                continue

            left = fixed + 1
            right = n - 1

            while left < right:
                cur_sum = nums[fixed] + nums[left] + nums[right]
                if cur_sum > 0:
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    solution.append([nums[fixed], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return solution

"""
it looks scary becuase of we need to use three numbers to find the target sum which is 0 in this case.
but we can still use the approach fo two sum problem which is use two pointers.

the idea is to have a fiex number and use two pointers to find the other two numbers and 3 adds up to 0
the logic is clear but in code we need to handle duplicates so we need more condion loops to skip dulicates.

since fixed is the first number, so we do a loop through 0 to n-2
the reason why we do n-2 is because we need at least two more numbers to find the target sum 
when entering the loop, we should check if the current fixed number is the same as previous fixed number
in the first iteration it will not happen so that is why we have condtion check fixed>0
if it is the same, we can skip this iteration by using continue, that cause fixed +=1

and if no duplicates or we alredy skipped the dulicates, we can initialize the left and right pointers
and then entern what we did in twp sum problem.

in this problem we do not only have one solution, so after we fid the solution we still need to move both pointers
to find if there is another solution for this fiex numer. 

to handle duplicates for left and right pointers, we can use while loop to skip the duplicates 
after we find a solution.

and after fixed reach n-2 we have found all the solution withouth duplicates and return it.
"""