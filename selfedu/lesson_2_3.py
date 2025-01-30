import numpy as np
import matplotlib.pyplot as plt


def act(x):
    return 1 if x >= 0 else 0


def go(C):
    x = np.array([C[0], C[1], 1])
    w1 = np.array([1, 1, -1.5])
    w2 = np.array([1, 1, -0.5])
    w_hidden = np.array([w1, w2])
    sum_hidden = np.dot(w_hidden, x)

    act_hidden = np.array([act(i) for i in sum_hidden] + [-1])

    w_hidden_2 = np.array([-1, 1, 0.5])
    res = np.dot(w_hidden_2, act_hidden)

    if act(res) == 1:
        print("Class 1")
    else:
        print("Class 2")


C1 = [(0, 1), (1, 0)]
C2 = [(0, 0), (1, 1)]
go(C1[0])
go(C1[1])

go(C2[0])
go(C2[1])
