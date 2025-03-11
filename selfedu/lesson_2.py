import numpy as np
import matplotlib.pyplot as plt

N = 5

x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10) / 10 for i in range(N)]
C1 = [x1, x2]

x1 = np.random.random(5)
x2 = x1 - [np.random.randint(10) / 10 for i in range(N)] - 0.1
C2 = [x1, x2]

f = [0, 1]

weights = np.array([-0.3, 0.3])
for i in range(N):
    x = np.array([C2[0][i], C2[1][i]])
    y = np.dot(x, weights)
    if y >= 0:
        print("Класс 1")
    else:
        print("Класс 2")

# plt.plot(C1[0][:], C1[1][:], s=10, c="red")
# plt.plot(C2[0][:], C2[1][:], s=10, c="blue")
# plt.plot(f)
# plt.grid(True)
# plt.show()
