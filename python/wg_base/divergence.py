import math

def divergence(w, d, n, lam):
    def get_angle(w):
        return w + 2 * d * math.tan(math.atan(lam / (math.pi * n * w)) / 2)
    return (get_angle(w) for w in w)