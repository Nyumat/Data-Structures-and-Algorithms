"""
Two Sum - #1 Leetcode.com
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution(object):
      def twoSum(self,nums,target):

            # Naive Approach O(n^2) time O(1) space
            """
            if not nums:
                  return []
            for i in range(len(nums)):
                  for j in range(len(nums) - 1):
                        if i == j:
                              return []
                        if nums[i] + nums[j] == target:
                              return [i,j]
                        else:
                              continue
            return [i,j]
            """
            """
            # Most common approach O(n) time O(n) space
            lib = {}
            for idx in range(len(nums)):
                  # Check for the compliment
                  pair = target - nums[idx]
                  # If the match is already in the dict return the indexes
                  if pair in lib:
                        return [lib[pair],idx]
                  # Otherwise, assign the non found index a key:value pair
                  lib[nums[idx]] = idx
            """
            # My favorite approach
            lookup = {}
            for index, num in enumerate(nums):
                  compliment  = target - num
                  if compliment in lookup:
                        return [lookup[compliment],index]
                  lookup[num] = index
            
if __name__ == "__main__":
      sol = Solution()
      nums = [1,2,5,9,6]
      target = 3
      target2 = 12
      answer2 = sol.twoSum(nums,target2)
      answer = sol.twoSum(nums,target)
      print(f'Nums: {nums}\nTarget: {target}\nAnswer: {answer} \n')
      print(f'Nums: {nums}\nTarget: {target2}\nAnswer: {answer2} \n')
