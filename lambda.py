g = lambda x: 3 * x + 1
print(g(5))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name("akash", "aj"))

sc = ['Akash mahmud Ja', 'Jinnat Sultana Vutu', 'Parvej Ahammad  Akash']

sc.sort(key=lambda name: name.split(" ")[-1].lower())

print(sc)


def build_quardric_fuction(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = build_quardric_fuction(10, 20, 30)
print(f(20))

import math


def radius(x):
    return math.pi * (x ** 2)


d = radius(10)
print(d)

dd = [10, 20, 25, 35, 70]

a = list(map(radius, dd))
print(a)

temps = [("Dhaka", 25), ("Chittagoong", 20), ("Chandpur", 29)]

c_to_f = lambda data: (data[0], 9 / 5 * data[1] + 32)

t = list(map(c_to_f, temps))

print(t)

import statistics as s

data = [10, 20, 10, 52, 11, 44, 44, 25, 4, 22, 78]

avg = s.mean(data)

print(avg)

lq = filter(lambda x: x > avg, data)

print(s.mean(list(lq)))

squars2 = [i ** 2 for i in range(1, 100)]

print(squars2)

A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 8, 10]

aa = [(a, b) for a in A for b in B]

print(aa)
