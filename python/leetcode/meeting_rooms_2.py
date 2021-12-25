'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 
Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

'''

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ordered = sorted(intervals)
        ends = []
        curr = max_num = 0
        for i, interval in enumerate(intervals):
            start, end = interval
            ends = [e for e in ends if e > start] + [end]
            curr = len(ends)
            max_num = max(max_num, curr)
        
        return max_num
        

s = Solution()
intervals = [[0,30],[5,10],[15,20]]
s.minMeetingRooms(intervals)