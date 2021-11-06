#from Lab2_closed_i import *
from Lab2_closed_1 import *
hs = HashTable()
'''
hs.add(0, 'ab', 347)
hs.print()
hs.add(1, 'cd', 472)
hs.print()
hs.add(8, 'ef', 101)
hs.print()

hs.add(11, 'aaa', 627)
hs.add(35, 'bbb', 695)
hs.add(4, 'ccc', 598)
hs.add(2, 'ddd', 597)
hs.add(3, 'eee', 596)
hs.print()

hs.delete(3)
hs.delete(35)
hs.print()

print(hs.get(11))
print(hs.get(0))
print(hs.get(22))
'''
import time
import random
for i in range(1000):
    b: bool = random.randint(0, 1)
    if b == 1:
        hs.add(i, 'example', 123)
hs.delete(0)
hs.delete(500)
hs.delete(999)
hs.add(0, 'aaa', 111)
hs.add(500, 'bbb', 222)
hs.add(999, 'ccc', 333)
print()

start = time.time()
print(hs.get(0))
result = time.time() - start
print("Program time: {:>.15f}".format(result) + " seconds.")

start1 = time.time()
print(hs.get(500))
result1 = time.time() - start
print("Program time: {:>.15f}".format(result) + " seconds.")

start2 = time.time()
print(hs.get(999))
result2 = time.time() - start
print("Program time: {:>.15f}".format(result) + " seconds.")


