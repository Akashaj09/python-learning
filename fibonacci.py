from functools import lru_cache

@lru_cache(maxsize = 1000)
def febonacci(n):
    if type(n) != int:
        raise TypeError('n must be positive number')
    if n < 1:
        raise ValueError('n must be positive int')
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return febonacci(n-1) + febonacci(n-2)

for n in range(1, 100):
    print(febonacci(n))