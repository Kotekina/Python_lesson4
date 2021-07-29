
from itertools import cycle

count = 0
for el in cycle("ABC"):
    if count >= 2:
     print(el)