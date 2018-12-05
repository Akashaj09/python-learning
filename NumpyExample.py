import numpy as np
import matplotlib.pyplot as plt
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
SIZE = 100
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

# numpy array methods
a = np.array([(1, 2, 3, 4), (5, 6, 7, 9)])
print([a[0, 2], a[1, 2]])
print(a[0:, 3])
print(a.ndim)
print(a.dtype)
print(a.size)
print(a.shape)
print(a.reshape(4, 2))
print(np.linspace(1, 5, 10))

b = np.array([(1, 58, 65), (28, 65, 28)])
c = np.array([(1, 58, 65), (28, 65, 28)])

print(np.vstack((b, c)))
print(np.hstack((b, c)))

print(b.ravel(2))

print(b.sum(axis=0))
print(b.sum(axis=1))

