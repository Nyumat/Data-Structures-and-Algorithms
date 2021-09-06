"""
217. Contains Duplicate
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        set1 = set(nums)
        return len(set1) != len(nums)
        
if __name__ == "__main__":
      sol = Solution()
      nums = [1, 2, 3, 1]
      print(f"Input: {nums}")
      output = sol.containsDuplicate(nums)
      print(f'Expected: True\nActual: {output}')
      # Other testcase
      nums = [1, 2, 3, 4]
      print(f"Input: {nums}")
      output = sol.containsDuplicate(nums)
      print(f'Expected: False\nActual: {output}')
