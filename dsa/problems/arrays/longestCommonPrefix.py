class Solution:
    def longestCommonPrefix(self, strs):
      strs.sort()
      res = []
      for i,c in enumerate(strs[0]):
        if c  == strs[-1][i]:
          res.append(c)
        else:
          break
        
      return ''.join(res)
        
      
if  __name__ == "__main__":
      sol = Solution()
      string = ["flower","flow","flight"]
      ans  = sol.longestCommonPrefix(string)
      print(f'Longest common prefix is: {ans}')