import numpy as np
from random import randint

class OrderedVector():
  def __init__(self, capacity):
    self.capacity = capacity
    self.lastPosition = -1
    self.values = np.empty(self.capacity, dtype=int)

  def show(self):
    if self.lastPosition == -1:
      print('Empty Vector')
    else:
      for i in range(self.lastPosition + 1):
        print(i, '', self.values[i])
      print()
  
  def insertValue(self, value):
    if self.lastPosition == self.capacity - 1:
      print('Capacidade máxima atingida')
      return

    pos = 0
    for i in range(self.lastPosition + 1):
      pos = i

      if self.values[i] > value:
        break
      
      if i == self.lastPosition:
        pos = i + 1

    x = self.lastPosition
    while x >= pos:
      self.values[x + 1] = self.values[x]
      x -= 1

    self.values[pos] = value
    self.lastPosition += 1

# arr = OrderedVector(10)

# arr.insertValue(5)
# arr.insertValue(3)
# arr.insertValue(6)
# arr.insertValue(10)

# arr.show()