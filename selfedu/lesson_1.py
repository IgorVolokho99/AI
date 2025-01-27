import numpy as np


def oct(x):
    return 0 if x < 0.5 else 1


def go(house, rock, attr):
    x_input = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12])
    weight2 = np.array([-1, 1])

    sum_hidden = np.dot(weight1, x_input)
    print("Сумма нейронов скрытого слов:", sum_hidden)

    hidden_output = [oct(x) for x in sum_hidden]
    print("Значение активаций нейронов скрытого слов:", hidden_output)

    last_output = np.dot(weight2, hidden_output)
    y = oct(last_output)
    print("Значение выходного словя:", y)

    return y


go(0, 1, 1)
