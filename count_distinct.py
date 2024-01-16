#   @Author BslWrz
#   @Date 2024/1/15

from cmath import sqrt
import random
import time

from datasketch import HyperLogLog


def countDistinct(lst, thresh):
    p = 1
    seen = set()
    for value in lst:
        seen.discard(value)
        if random.random() < p:
            seen.add(value)
        if len(seen) == thresh:
            seen = set(filter(lambda x: random.random() < 0.5, seen))
            p *= 0.5
    return len(seen) / p


MAXX = 1000000
lst = [random.randint(1, MAXX) for _ in range(MAXX)]
# print(lst)
t1 = time.time()
print('without hash\t', countDistinct(lst, sqrt(MAXX)))
t2 = time.time()
print(t2 - t1)

count = len(set(lst))
t3 = time.time()
print('set(accurate)\t', count)
print(t3 - t2)

# hl = HyperLogLog()
# for value in lst:
#     hl.update(str(value).encode('utf-8'))
# t4 = time.time()
# print('hll\t\t\t\t', hl.count())
# print(t4 - t3)
