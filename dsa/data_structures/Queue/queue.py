class Queue:
      def __init__(self, size):
            self.size = size
            self.queue = [None for i in range(size)]
            self.front = self.rear = -1
      def enqueue(self, item):
            if ((self.rear + 1) % self.size == self.front): # Queue is full
                  return None
            elif self.front == -1:  # Empty queue
                  self.front = 0
                  self.rear = 0
                  self.queue[self.rear] = item # Add the item to the queue. (FIFO)
            else: # Items already in the queue
                  self.rear = (self.rear + 1) %  self.size
                  self.queue[self.rear] = item
      def dequeue(self):
            if (self.front == -1): # Empty
                  return None
            elif (self.front == self.rear): # One element
                  tmp = self.queue[self.front]
                  self.front = -1
                  self.rear = -1
                  return tmp
            else: # > 1 Element
                  tmp = self.queue[self.front]
                  self.front = (self.front + 1) % self.size
                  return tmp
      def get_size(self):
            if (self.front == -1):
                  