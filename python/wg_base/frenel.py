import math


def reflection(alpha, n1, n2):
    cos = math.cos
    sin = math.sin
    sqrt = math.sqrt
    return (n1 * cos(alpha) - sqrt(n2 ** 2 - (n1 * sin(alpha)) ** 2)) ** 2 / \
           (n1 * cos(alpha) + sqrt(n2 ** 2 - (n1 * sin(alpha)) ** 2)) ** 2


def transmission(alpha, n1, n2):
    cos = math.cos
    sin = math.sin
    sqrt = math.sqrt
    return (4 * n1 * cos(alpha) * sqrt(n2 ** 2 - (n1 * sin(alpha)) ** 2)) / \
           (n1 * cos(alpha) + sqrt(n2 ** 2 - (n1 * sin(alpha)) ** 2))**2