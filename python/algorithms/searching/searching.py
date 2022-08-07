import random

class Searching(object):
      def linear_search(self,unsorted,sorted,target):
            for i in range(len(unsorted)):
                  if unsorted[i] == target:
                        return i
            return -1
      def binary_search(self,sorted,target):
            l = 0
            r = len(sorted)
            while (l < r):
                  midpoint = l + (r - l) // 2
                  if sorted[midpoint] == target:
                        return midpoint
                  elif sorted[midpoint] < target:
                        r = midpoint
                  else:
                        l = midpoint + 1
            return midpoint
      def depthFirstSearch(self,root):
            # Using a stack
            stack = [root]
            while stack:
                  current = stack.pop()
                  print(current)
                  if current.right is not None: stack.append(current.right) 
                  if current.left is not None: stack.append(current.left)
      def depthFirstSearchRecursive(self,root):
            if root == None:
                  return 
            print(root)
            self.depthFirstSearchRecursive(root.left)
            self.depthFirstSearchRecursive(root.right)

if __name__ == "__main__":
      sol = Searching()
      sorted = [0,1,2,3,4,5]
      unsorted = [1,5,2,3,6,2]
      linear = sol.linear_search(unsorted,sorted,2)
      binary = sol.binary_search(sorted,2)

      print(linear)
      print(binary)
