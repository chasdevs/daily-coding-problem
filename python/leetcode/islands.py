'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

'''
Brainstorm:

Edge cases:
grid = [
  ['1']
]
answer: 1

grid = [
  ['0']
]
answer: 0

grid = [
  ['1', '0', '1', '0', '1']
]
answer: 3

Naive:
- Start scanning array left-to-right, top-to-bottom looking for first piece of land.
  - Once land is found, "explore" that piece of land until it has been discovered.. can call this island int(1)
  - Either store results in new grid (as 1's since it is island 1) or rename the explored pieces.
- Continue scanning grid from where we left off; looking for next piece of land ('1').
  - Repeat exploration step, setting island number x:
    - explore(i,j,x):
       # Look above (i-1, j), below (i+1, j), left (i, j-1), right (i, j+1) # Recursive; explore above/below/left/right # TODO: Edges
       # If '1':
        # "Claim" i,j and then recursively explore above/below/left/right. # TODO: Dynamic Programming? State is [m][n]
       # If '0':
       #   pass
- Complexity: m*n

'''

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        island = 0

        for i in range(0, self.m):
          for j in range(0, self.n):
            cell = grid[i][j]
            is_land = cell=='1'
            if is_land:
              island+=1
              self.explore(i,j,island)
        
        return island

    def explore(self, i, j, island):
      if i < 0 or j < 0 or i >= self.m or j >= self.n:
        return

      if self.grid[i][j] == '1':
        self.grid[i][j] = island
        self.explore(i-1, j, island)
        self.explore(i+1, j, island)
        self.explore(i, j-1, island)
        self.explore(i, j+1, island)

s = Solution()
grid = [
  ["0"],
]
s.numIslands(grid)