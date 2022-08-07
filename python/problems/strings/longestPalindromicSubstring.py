class Solution(object):
      def longestPalindrome(self, s):
            n = len(s)
            answer = ""
            for i in range(n):
                  even = self.expand(s,i,i)
                  odd = self.expand(s,i,i+1)
                  answer = max(even,odd,answer,key=len)
                  
            return answer
      def expand(self, s, left , right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                  left -= 1
                  right += 1
                  print(s[left + 1: right])
            return s[left + 1: right]
if __name__ == "__main__":
      sol = Solution()
      string = "babad"
      ans = sol.longestPalindrome(string)
      print(f"Longest palindromic substring is: {ans}")