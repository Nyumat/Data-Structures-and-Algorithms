"""
Number of Islands - #200 Leetcode.com
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""

class Solution(object):
      def countIslands(self, graph):
            numIslands = 0
            if not graph:
                  return numIslands
            for i in range(len(graph)):
                  for j in range(len(graph[0])):
                        if graph[i][j] == "1":
                              self.depthFirstSearch(graph,i,j)
                              numIslands += 1
            return numIslands
      def depthFirstSearch(self,graph, rows, cols):
            # Exit condition
            if rows < 0 or rows >= len(graph) or cols < 0 or cols >= len(graph[0]):
                  return
            if graph[rows][cols] == "1":
                  #Set to 0 to avoid double counting
                  graph[rows][cols] = "0"
                  self.depthFirstSearch(graph,rows + 1, cols)
                  self.depthFirstSearch(graph,rows - 1, cols)
                  self.depthFirstSearch(graph, rows, cols + 1)
                  self.depthFirstSearch(graph, rows, cols - 1)
if __name__ == "__main__":
      import numpy as np
      sol = Solution()
      inp = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
      expected = 1
      ans = sol.countIslands(inp)
      print(f'Input:\n{np.matrix([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])}\nExpected: 1\nActual: {ans}')
      
