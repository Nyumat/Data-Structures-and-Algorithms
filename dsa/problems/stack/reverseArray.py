
class Solution:
      def reverseArray(self, arr):
            stack = []
            res = []
            for i in arr:
                  stack.append(i)
            for j in range(len(arr)):
                  res.append(stack.pop())
            return res

arr = [1, 2, 3, 4, 4]
ans = Solution()
print(ans.reverseArray(arr))

