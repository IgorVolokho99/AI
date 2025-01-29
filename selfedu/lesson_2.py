import numpy as np

N = 5
x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10) / 10 for _ in range(N)]
C1 = [x1, x2]

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10) / 10 for _ in range(N)] - 0.1
C2 = [x1, x2]

f = [0, 1]

w = np.array([-0.3, 0.3])

for i in range(N):
    x_input = np.array([C2[0][i], C2[1][i]])
    s = np.dot(w, x_input)

    if s >= 0:
        print("Класс 1")
    else:
        print("Класс 2")
