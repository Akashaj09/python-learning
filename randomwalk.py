import random
from functools import lru_cache


@lru_cache(maxsize=2000000000000)
def random_walk(n):
    x, y = 0, 0
    for i in range(n):
        step = random.choice(['n', 's', 'e', 'w'])
        if(step == 'n'):
            y += 1
        elif step == 's':
            y -= 1
        elif step == 'e':
            x += 1
        else:
            x -= 1
    return (x, y)

@lru_cache(maxsize=2000000000000)
def random_walk2(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy

    return (x, y)


for i in range(20000000):
    walk = random_walk2(10)
    print(walk, "Distance from home: ", abs(walk[0]) + abs(walk[1]))