
# Count the number of trailing 0s in factorial of a given number.

import math

tc = int(input())

for _ in range(tc):
    n = int(input())
    i = 5
    count = 0
    while (n / i) >= 1:
        count = count + math.floor(n / i)
        i = i * 5
    print(count)
