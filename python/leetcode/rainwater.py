'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
 
Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

'''
start pointer to max left height at left l with height ML
start pointer at end of heights r with height MR

if any height H is less than ML and MR, that "depth" of min(ML, MR)-H is added to total water
can scan from l to r unless ML exceeds MR, at which point you need to scan from r to l

vars:
 max left: L
 left index: l
 max right: R
 right index: r
 current height: H
 current index: i

l=0
L=heights[l]

r=len(heights)-1
R=heights[r]




  x
x x
xxxx 
xxxxxx x
01234567
l      r
l     i
l    i
l   i
l  i
L>R, so start scanning from right:
  i = r-1
  H < R, so add depth to sum S
  i = r-2
  H == R, so add depth 0 to sum S
  ...
  i = r-4
  H > R

'''

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        S = 0
        ML = 0
        MR = 0

        while l <= r:
            L = height[l]
            R = height[r]
            if L <= R:
                if L >=ML: ML = L
                else: S += ML - L
                l+=1
            else:
                if R>=MR: MR = R
                else: S += MR - R
                r-=1

        print(S)


'''
x    x
xx   x
xxx xxx x

l       r # L > R. Set MR=1, decrement r
l      r  # R < MR. Add sum. decrement r
l     r   # R == MR. Do nothing. decrement r
l    r    # R > MR. R==L. Set MR=3. increment l
 l   r    # L < ML. Add sum. increment l
  l 


'''
            

s = Solution()
height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
s.trap(height)