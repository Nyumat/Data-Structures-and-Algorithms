class Stack: # Wrapper
      def __init__(self): # List in python are the foundation of the stack 
            self.stack = list()
      def push(self, item): # Add an item to the top of our stack
            self.stack.append(item)
      def pop(self):
            if len(self.stack) > 0:
                  return self.stack.pop()
            else: # To avoid exceptions (empty stack)
                  return None
      def peek(self):
            if len(self.stack) > 0: # Return the  item on the top of our stack
                  return self.stack[len(self.stack) - 1]
            else:
                  return None
      def __str__(self):  # Print the stack
            return str(self.stack)
def main():
      stack = Stack()
      for i in range(15):
            stack.push(i)
            print("Adding: " + str(i))
      print(stack)
      print("Peeking Stack:", stack.peek())
      print("Popping Stack's top element:", stack.pop())
