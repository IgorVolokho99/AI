import numpy as np

N = 5
b = 3

x1 = np.random.random(5)
x2 = x1 + [np.random.randint(10) / 10 for _ in range(5)] + b
C1 = [x1, x2]

x1 = np.random.random(5)
x2 = x1 - [np.random.randint(10) / 10 for _ in range(5)] - b - 0.1
C2 = [x1, x2]

w1 = -0.3
w2 = -w1
w3 = -b * w2
weights = np.array([w1, w2, w3])
for i in range(N):
    x = np.array([C2[0][i], C2[1][i], 1])
    y = np.dot(x, weights)
    if y >= 0:
        print("Класс 1")
    else:
        print("Класс 2")
