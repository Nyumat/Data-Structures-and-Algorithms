
"""
Move Zeros - #283 Leetcode.com

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

class Solution(object):
    def moveZeroes(self, nums):
        temp = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[temp] = nums[temp], nums[i]
                temp += 1
if __name__ == "__main__":
      solution = Solution()
      print(f'\nArray before exe:[1, 2, 0, 5, 0, 0, 7, 0]\n')
      nums = [1,2,0,5,0,0,7,0]
      solution.moveZeroes(nums)
      print(f'After: {nums}\n')

    

