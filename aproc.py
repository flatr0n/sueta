import math
import random
import numpy as np


def f(xp):
    return ((math.exp(xp) + math.exp(-xp)) ** math.sin(xp)) * (1 / (xp ** 4 + 3))


def get_y(rnd_padding=False):
    return [f(yi) + random.uniform(-0.1, 0.1) if rnd_padding else f(yi) for yi in x]


x = [x for x in np.arange(0, 2.1, 0.1)]

valid_y = get_y()


def calc_params(data_x, data_y):
    size = len(data_x)
    i = 0
    sum_x = 0
    sum_sqare_x = 0
    sum_third_power_x = 0
    sum_four_power_x = 0
    sum_y = 0
    sum_xy = 0
    sum_sqare_xy = 0
    while i < size:
        sum_x += data_x[i]
        sum_y += data_y[i]
        sum_sqare_x += data_x[i] ** 2
        sum_third_power_x += data_x[i] ** 3
        sum_four_power_x += data_x[i] ** 4
        sum_xy += data_x[i] * data_y[i]
        sum_sqare_xy += data_x[i] ** 2 * data_y[i]
        i += 1
    return np.linalg.solve(np.array([[size, sum_x, sum_sqare_x],
                                     [sum_x, sum_sqare_x, sum_third_power_x],
                                     [sum_sqare_x, sum_third_power_x, sum_four_power_x]]), np.array([sum_y, sum_xy, sum_sqare_xy]))


def calc_y(data_x, params):
    datay = []
    for x in data_x:
        datay.append(params[2] * x ** 2 +
                     params[1] * x + params[0])
    return datay


def get_data():
    rnd_y = get_y(rnd_padding=True)
    params = calc_params(x, rnd_y)
    aproc_y = calc_y(x, params)
    return rnd_y, aproc_y
