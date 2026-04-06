"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

Constraints:

1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1

"""

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[0])
        arrows = 1
        arrow_pos = points[0][1]
    
        for i in range(1, len(points)):
            if points[i][0] > arrow_pos:   # new group!
                arrows += 1
                arrow_pos = points[i][1]
            else:
                arrow_pos = min(arrow_pos, points[i][1])  # shrink window
    
        return arrows
        
        
        
"""
Think about it visually:
[1,6]
[2,8]
The arrow must hit both — so it must be within 1-6 AND within 2-8. The overlapping region is [2,6]. So the arrow can be anywhere from 2 to 6.
But to be safe for future balloons, you want to shoot as early as possible — so track the min of ends! That way the arrow stays as far left as possible, giving more chance to hit future balloons.
So the rule is:

Sort by xstart
Track arrow_pos = min of ends in current group
If next balloon's xstart > arrow_pos → it's a new group, need a new arrow!

points[i][0] > arrow_pos
And the three conditions:

New group → arrows += 1, arrow_pos = points[i][1] (new arrow at new balloon's end)
Same group → arrow_pos = min(arrow_pos, points[i][1]) (shrink the window)


dry run Example 1 after sorting [[1,6],[2,8],[7,12],[10,16]]:

arrow_pos = 6, arrows = 1
[2,8]: 2 <= 6 → same group! arrow_pos = min(6,8) = 6
[7,12]: 7 > 6 → new group! arrows = 2, arrow_pos = 12
[10,16]: 10 <= 12 → same group! arrow_pos = min(12,16) = 12

Result: 2
"""

