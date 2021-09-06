
class Solution:
      def interpret(self, command):
            lookup = {"G":"G","()":"o","(al)":"al"}
            n = len(command)
            res = ""
            i = 0
            while i < n:
                  for index, value in enumerate(command):
                        if value == "(" and command[index + 1] == "a":
                              res += lookup["(al)"]
                        if value == "(" and command[index+1] != "a":
                              res += lookup["()"]
                        if value == "G":
                              res += "G"
                        i+=1
            print(res)
sol = Solution()
command = "G()(al)"
sol.interpret(command)
