from timeit import Timer
import random

# popzero = Timer('x.pop(0)', 'from __main__ import x')
# popend = Timer('x.pop()', 'from __main__ import x')

# print("pop(0)   pop()")
# for i in range(int(10e+6), int(10e+7) + 1, int(10e+6)):
#     x = list(range(i))
#     pt = popend.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print('%15.5f, %15.5f' % (pz, pt))

for i in range(10000, 1000001, 20000):
    t = Timer('random.randrange(%d) in x' % i, 'from __main__ import random, x')
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print('%d, %10.3f, %10.3f' % (i, lst_time, d_time))
