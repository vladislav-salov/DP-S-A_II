from Lab2_chain2 import *

hs = HashTable()
'''
hs.add(1, 'ab', 'gh')
hs.print()
hs.add(2, 'cd', 'ij')
hs.print()
hs.add(5, 'ef', 'kl')
hs.print()

hs.add(7, 'abc', 'pqr')
hs.add(9, 'def', 'stu')
hs.add(12, 'ghi', 'vwx')
hs.add(13, 'jkl', 'yza')
hs.add(14, 'mno', 'bcd')
hs.print()

hs.remove(12)
hs.remove(5)
hs.print()

print(hs.get(9))
print(hs.get(2))
print(hs.get(5))'''
'''
import time
import random
for i in range(10000):
    b: bool = random.randint(0, 1)
    if b == 1:
        hs.add(i, 'example', 'example')
hs.add(0, 'aaa', 'ddd')
hs.add(5120, 'bbb', 'eee')
hs.add(9999, 'ccc', 'fff')
print()

start = time.time()
print(hs.get(0))
result = time.time() - start
print("Program time: {:>.5f}".format(result) + " seconds.")

start = time.time()
print(hs.get(5120))
result = time.time() - start
print("Program time: {:>.5f}".format(result) + " seconds.")

start = time.time()
print(hs.get(9999))
result = time.time() - start
print("Program time: {:>.5f}".format(result) + " seconds.")'''


