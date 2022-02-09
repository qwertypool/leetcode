452. Minimum Number of Arrows to Burst Balloons
Medium
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 
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
  
 ===================================================================================
# Approach 1:
class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key = lambda s: s[1])
        l = len(points)
        current = points[0]
        count = 1
        
        for i in range(l):
            if current[1] < points[i][0]:
                current = points[i]
                count += 1
        
        return count
