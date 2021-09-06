class Solution:
      def duplicateZeros(self, nums):
            shift = 0
            n = len(nums)
            while shift < n:
                  if nums[shift] == 0:
                        nums.insert(shift + 1, 0) # Insert a Zero in the i + 1 element
                        nums.pop() # Remove the element at the end to make 
                        shift += 1
                  shift += 1
nums = [1,0,2,0,4,5,0]
solution = Solution()
solution.duplicateZeros(nums)
print(nums)