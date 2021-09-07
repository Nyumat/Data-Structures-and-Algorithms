# basic array (list in python) 
one_d_array = []

# Add values
import random
to_append = random.randint(0,10)
one_d_array.append(to_append)

# Get the length of an array using len()
print(f'Length of 1-D Array: {len(one_d_array)}')

# Add values using while loop
goal_length = 10
while len(one_d_array) != goal_length:
      one_d_array.append(to_append)
      break

# list comprehension to create a m x n matrix full of zeros
m = 4
n = 4
two_d_array = [[0] * m for _ in range(n)]

# Iterate through the values
for integer in one_d_array:
      print(integer)

# Iterate through the indexes
for index in range(len(one_d_array)):
      print(index)

# Enumeration allows us to traverse both
for index, number in enumerate(one_d_array):
      print(f'Index: {index}, Number: {number}')

# Traverse the 2-Dimensional Array values
for row in range(m):
      for column in range(n):
            print(two_d_array[row][column])
