import math
import itertools
class square:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= N:
        x = self.a
        self.a += 1
        return x


N = int(input())
myclass = square()
myiter = iter(myclass)

for x in myiter:
  print(x)     