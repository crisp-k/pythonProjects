# infinite.py
from itertools import count

for n in count(5,3):
    if n > 1000000:
        break
    print(n, end=', ')