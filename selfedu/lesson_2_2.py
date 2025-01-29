import numpy as np

N = 5
b = 3

x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10) / 10 for _ in range(N)] + b
C1 = [x1, x2]

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10) / 10 for _ in range(N)] + b - 0.1
C2 = [x1, x2]

f = [0 + b, 1 + b]

w2 = 0.3
w3 = -b * w2
weights = np.array([-w2, w2, w3])

for i in range(N):
    x_input = np.array([C2[0][i], C2[1][i], 1])
    s = np.dot(weights, x_input)

    if s >= 0:
        print("C1")
    else:
        print("C2")