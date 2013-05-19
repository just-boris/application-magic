import math

def divergence(w, d, lam):
    def get_angle(w):
        return w * math.sqrt(1 + (d * lam / (math.pi * w**2))**2)
    return (get_angle(w) for w in w)