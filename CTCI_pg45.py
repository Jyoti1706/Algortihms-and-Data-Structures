'''
Print all the positive integer  solution to the equation
a^3+b^3=c^3+d^3
'''
import math

cd_hashmap = {}
for c in range(1,5):
    for d in range(1,5):
        result = math.pow(d,3)+math.pow(c,3)
        cd_hashmap[result] = [c,d]

for result, pair in cd_hashmap.items():
    for pair1 in pair:
        for pair2 in pair:
            print(pair1,pair2)
