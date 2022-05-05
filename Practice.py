import numpy as np

array_1 = np.array([[1, 2, 7], [3, 4, 8]])
array_2 = np.array([[1, 2], [3, 9], [4, 16]])

print(np.dot(array_1, array_2))

for i in [0,2,3]:
    if i%2 == 0:
        print("even")
    elif i == 0:
        print("zero")
    else:
        print("odd")