"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
    
        for curr in intervals[1:]:
            prev = result[-1]
            if prev[1] >= curr[0]:        # overlap!
                prev[1] = max(prev[1], curr[1])  # merge
            else:
                result.append(curr)
    
        return result
        
"""
first we need to sort all the intervals. by doing this, we sort by the head of each intervals
and next is how do we know if an invertal have overlapping is by comparing the tails of previous and head of current
if tail is larger than head then there are overlap. and for the new merged tail we take the max of two tails.
and that is our new interval. and if not, we move on. untill we finish all intervals

"""


