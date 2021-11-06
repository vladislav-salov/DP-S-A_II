from Lab2_chain1 import *

hs = HashTable()
'''
hs.add(1, 'ab')
hs.print()
hs.add(2, 'cd')
hs.print()
hs.add(5, 'ef')
hs.print()

hs.add(7, 'abc')
hs.add(9, 'def')
hs.add(12, 'ghi')
hs.add(13, 'jkl')
hs.add(14, 'mno')
hs.print()

hs.remove(12)
hs.remove(5)
hs.print()

print(hs.get(9))
print(hs.get(2))
print(hs.get(5))
'''
import time
import random
for i in range(10000):
    b: bool = random.randint(0, 1)
    if b == 1:
        hs.add(i, 'example')
hs.add(0, 'aaa')
hs.add(4998, 'bbb')
hs.add(9999, 'ccc')
print()

start = time.time()
print(hs.get(0))
result = time.time() - start
print("Program time: {:>.5f}".format(result) + " seconds.")

start = time.time()
print(hs.get(4998))
result = time.time() - start
print("Program time: {:>.5f}".format(result) + " seconds.")

start = time.time()
print(hs.get(9999))
result = time.time() - start
print("Program time: {:>.5f}".format(result) + " seconds.")


