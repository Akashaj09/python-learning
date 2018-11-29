# map filter and reduce
import statistics

rad = [10, 20, 25, 30, 45, 255, 65, 85]
print(list(map(lambda x: x**2, rad)))
avg = statistics.mean(rad)
print(list(filter(lambda x: x < avg, rad)))