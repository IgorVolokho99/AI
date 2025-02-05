import numpy as np


def act(x: float) -> int:
    return 1 if x <= 0 else 0


def check_xor(x: float, y: float) -> int:
    x_input = np.array([x, y, 1])
    w_1 = [1, 1, -1.5]
    w_2 = [1, 1, -0.5]
    w_hidden = np.array([w_1, w_2])
    w_out = np.array([-1, 1, 0.5])

    x_sum_1 = np.dot(w_hidden, x_input)
    x_out_1 = [act(x) for x in x_sum_1]
    x_out_1.append(1)
    x_out_1 = np.array(x_out_1)

    x_sum_2 = np.dot(w_out, x_out_1)
    res = act(x_sum_2)

    return res


print(check_xor(1, 0))
