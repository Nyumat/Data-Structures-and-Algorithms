# basic linkedlist interface

class Node:
      def __init__(self, value):
            self.value = value
            self.next = None
      def append_tail(self, value):
            curr = self
            while curr:
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

