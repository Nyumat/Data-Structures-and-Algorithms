# basic linkedlist interface

class Node:
      def __init__(self, value):
            self.value = value
            self.next = None
      def append_tail(self, value):
            curr = self
            while curr.next:
                  curr = curr.next
            curr.next = Node(value)
      def get_at_index(self, index):
            curr = self
            while curr and index:
                  curr = curr.next
                  index = index - 1
            if curr: # Found
                  return curr.value
            else: # Not found
                  return None
      def delete_by_value(self, value):
            curr = self
            while curr and curr.next:
                  if curr.next == value:
                        curr.next = curr.next.next
                  curr = curr.next
if __name__ == "__main__":
      our_list = Node(1)
      our_list.append_tail(2)
      our_list.append_tail(3)
      print(f' Value at index 1: {our_list.get_at_index(1)}')
      while our_list != None:
            print(our_list.value)
            our_list = our_list.next