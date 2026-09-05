# How to calculate execution time in python

import time

start_time = time.perf_counter()

for i in range(10000000):
    pass

end_time = time.perf_counter()

elasped_time = end_time - start_time

print(f"The Elasped Time: {elasped_time} seconds")

