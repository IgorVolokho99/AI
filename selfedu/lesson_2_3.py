import numpy as np


def oct(x):
    return 0 if x < 0 else 1


def go(C):
    x_1 = np.array([C[0], C[1], 1])
    w_1 = np.array([[1, 1, -1.5], [1, 1, -0.5]])
    sum_1 = np.dot(w_1, x_1)
    y_1 = np.array([oct(x) for x in sum_1] + [1])

    x_2 = y_1
    w_2 = np.array([-1, 1, -0.5])
    sum_2 = np.dot(w_2, x_2)
    y = oct(sum_2)
    return y


tests = ((0, 1, 1), (0, 1, 1), (1, 1, 0), (0, 0, 0))

for test in tests:
    res = go(test[:2])
    if res == test[-1]:
        print(f"Угадал, это был класс: {test[-1]}")
    else:
        print(f"Не угадал, это был класс: {test[-1]}")

