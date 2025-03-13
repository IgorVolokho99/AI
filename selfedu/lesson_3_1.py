import numpy as np


def f(x):
    return 2 / (1 + np.exp(-x)) - 1


def df(x):
    return 0.5 * (1 + x) * (1 - x)


W1 = np.array([[-0.267867, 0.6, -0.4], [0.567, -0.3876, -0.84]])
W2 = np.array([0.6, -0.3])


def go_forward(inp):
    sum1 = np.dot(W1, inp)
    out1 = np.array([f(x) for x in sum1])

    sum2 = np.dot(W2, out1)
    y = f(sum2)

    return y, out1


def train(epoch):
    global W1, W2
    lmd = 0.05
    N = 1_000_000
    count = len(epoch)
    for i in range(N):
        x = epoch[np.random.randint(0, count)]
        y, out = go_forward(x[0:3])
        e = y - x[-1]
        delta = e * df(y)
        W2[0] = W2[0] - lmd * delta * out[0]
        W2[1] = W2[1] - lmd * delta * out[1]

        delta2 = W2 * delta * df(out)

        W1[0, :] = W1[0, :] - lmd * delta2[0] * np.array(x[0:3])
        W1[1, :] = W1[1, :] - lmd * delta2[1] * np.array(x[0:3])


epoch = [
    (-1, -1, -1, -1),
    (-1, -1, 1, 1),
    (-1, 1, -1, -1),
    (-1, 1, 1, 1),
    (1, -1, -1, -1),
    (1, -1, 1, 1),
    (1, 1, -1, -1),
    (1, 1, 1, -1)
]

train(epoch)

for x in epoch:
    y, out = go_forward(x[0:3])
    print(f"Полученный результат НС: {y} -> {x[-1]}")
