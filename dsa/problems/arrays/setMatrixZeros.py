"""
Set Matrix Zeros - #73 Leetcode.com

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.
"""

class Solution(object):
      def setZeroes(self, matrix):
            """
            :type matrix: List[List[int]]
            :rtype: None Do not return anything, modify matrix in-place instead.
            """
            rows = []
            cols = []
            for i in range(len(matrix)):
                  for j in range(len(matrix[0])):
                        if matrix[i][j] == 0:
                              rows.append(i)
                              cols.append(j)
            for row in rows:
                  # Add 0's the length of the column
                  matrix[row] = [0] * len(matrix[0])
            for col in cols:
                  for row in range(len(matrix)):
                        matrix[row][col] = 0
if __name__ == "__main__":
      import numpy as np
      sol = Solution()
      the_matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
      expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
      print(f' Your Input: \n{np.matrix(the_matrix)}')
      sol.setZeroes(the_matrix)
      if the_matrix == expected:                  
            print(f'Expected:\n{np.matrix(expected)}\nOutput:\n{np.matrix(the_matrix)}\nStatus: PASSED')
      else:
            print("Testcase failed.")

