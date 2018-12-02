import numpy as np
import sys
import time

# num py array example
ar = np.array([(1, 2, 3), (3, 4, 6, 8, 12)])
print(ar)

# numpy array  size comparision with list
S = range(1000)
print(sys.getsizeof(5) * len(S))
D = np.arange(1000)
print(D.size * D.itemsize)
# numpy array speed comparision example
SIZE = 10000000
# normal list
l1 = range(SIZE)
l2 = range(SIZE)
# numpy list
np1 = np.arange(SIZE)
np2 = np.arange(SIZE)
# normal list comparision
start = time.time()
result = [(x, y) for (x, y) in zip(l1, l2)]
print(result)
print((time.time() - start) * 1000)
# numpy array comparision
start = time.time()
result = np1 + np2
print(result)
print((time.time() - start) * 1000)
