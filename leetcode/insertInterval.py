"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
    
        for interval in intervals:
            if interval[1] < newInterval[0]:      # completely before
                result.append(interval)
            elif interval[0] > newInterval[1]:    # completely after
                result.append(newInterval)
                newInterval = interval
            else:                                  # overlap!
                newInterval = [min(interval[0], newInterval[0]), 
                                max(interval[1], newInterval[1])]
    
        result.append(newInterval)
        return result
    
"""
the intervals are alredy sorted so what we need to think is the condition when do we insert or merge
interval[1] < newInterval[0] if the tail is smaller than newinterval head, we insert as it
interval[0] > newInterval[1] if the head is bigger than newinterval tail, we insert as it
else, there are overlap. so we need to merge. and use the min of these two interval as head. max of these two intervals as tail

"""

