import time
import random
import sys

sys.set_int_max_str_digits(1000000)

num = 4300

# n = int("123456789")
S = "1"
for i in range(num):
    S += str(random.randint(0, 9))
start_time = time.time()
A = int(S)
end_time = time.time()
print("Time elapsed:", end_time - start_time, "seconds.")
