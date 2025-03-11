import numpy as np


def oct(x):
    return 0 if x < 0.5 else 1


def go(house, rock, attr):
    x_input_1 = np.array([house, rock, attr])
    w1 = np.array([[0.3, 0.4, 0], [0.4, -0.5, 1]])
    w2 = np.array([-1, 1])
    x_input_2 = np.dot(w1, x_input_1)
    y_output_2 = np.array([oct(x) for x in x_input_2])
    x_input_3 = np.dot(y_output_2, w2)

    out = oct(x_input_3)

    return out


print(go(1, 0, 0))
