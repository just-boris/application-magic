import math

def divergence(w, d, n, lam):
    def get_angle(w):
        return w + d * lam / (math.pi * n * w)
    return (get_angle(w) for w in w)