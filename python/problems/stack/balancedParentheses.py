

# ()(()
# ()(())

class Solution:
      def balancedParantheses(self, arr):
            lookup = {"(":")"}
            stack = []
            for para in arr:
                  if para in lookup:
                        stack.append(para)
                  else:
                        if stack == [] or lookup[stack.pop()] != para: # Watch logic here
                              return False
            return stack == []           

            

if __name__ == "__main__":              

      arr = "()()()"
      arr2 = "()(()"

      sol = Solution()

      ans = sol.balancedParantheses(arr)
      ans2 = sol.balancedParantheses(arr2)

      print(ans)
      print(ans2)
