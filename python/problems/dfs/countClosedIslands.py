"""
#1254 - Number of Closed Islands
Medium
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.
"""
# Time (O mn)
# Space (O mn)
class Solution(object):
      def closedIsland(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            rows = len(grid)
            cols = len(grid[0])
            if not grid:
                  return 0
            numIslands = 0
            for i in range(rows - 1):
                  for j in range(cols - 1):
                        if (grid[i][j] == 0):
                              if (self.isClosed(grid, i, j, rows, cols)):
                                    numIslands += 1
            return numIslands
      def isClosed(self, grid, i, j, rows, cols):
            # -1 visited
            # 1 = water
            # 0 = land
            if (grid[i][j] == -1 or grid[i][j] == 1):
                  return True
            if (self.isEdge(i, j, rows, cols)):
                  return False
            # If it makes it past both then we change curr to -1
            grid[i][j] = -1
            # Now we check the directions
            left = self.isClosed(grid, i, j-1, rows, cols)
            right = self.isClosed(grid, i, j+1, rows, cols)
            up = self.isClosed(grid, i-1, j, rows, cols)
            down = self.isClosed(grid, i+1, j, rows, cols)
            # Return false if one of these are not true using bool logic
            return left and right and up and down
      def isEdge(self, i, j, rows, cols):
            # Check if the current point is on the edge, which means it isnt possible for there to be a closed island
            return i == 0 or j == 0 or i == rows - 1 or j == cols - 1
if __name__ == "__main__":
      import numpy as np
      sol = Solution()
      data = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
      print(f"Before execution:\n{np.matrix(data)}")
      output = sol.closedIsland(data)
      print(f"After execution:\n{np.matrix(data)}\nExpected: 2\nActual: {output}")
