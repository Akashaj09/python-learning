import math
#  import time

def python_prime(n):
    if(n == 1):
        return False  # 1 is not a pri me number

    if n > 2 & n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return  False
        else:
            return True


#t0 = time.time()
for n in range(2 , 10000):
    print(n, ' : ',python_prime(n))
#t1 = time.time()

#print(t1-t0)