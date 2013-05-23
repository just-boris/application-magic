# coding=utf-8
import math
import main
import numpy as np
import pylab
from wg_base.coupling import coupling
from planar import Planar
from gauss import Gauss
import angular_bevel

r = main.wg_radius[u'ОВССП']
w = (r, r)
lam = 1.55
n = 1.47

planar = Planar(open('matrix/dump2d.csv'))
reflection_cylinder = Gauss(*w, a=0, b=main.max_coupling_point)

div_angle = 2 * lam / (math.pi * r ** 2)
fi_min = 0
fi_max = 45

def toRadians(fi):
    return fi * math.pi / 180

def transmission(fi):
    result = angular_bevel.angular_yz(fi) * (1 - backreflection(fi))
    if result > transmission.max:
        transmission.max = result
        transmission.arg = fi
    return result

def backreflection(fi):
    d = 2 * toRadians(fi / 2) * r / div_angle
    cylinder = Gauss(*w, a=0, b=main.max_coupling_point - d)
    return coupling(reflection_cylinder.func, cylinder.func)

transmission.max = 0
x_range = np.arange(fi_min, fi_max, 0.1)
pylab.plot(x_range, [transmission(x) for x in x_range], 'k', label=u'Передача')
pylab.plot(x_range, [backreflection(x) for x in x_range], 'k--', label=u'Отражение')
pylab.legend()
pylab.grid()
print transmission.max, transmission.arg
main.arrow_axes((fi_min, fi_max), (0, 1), "$\phi,{}^\circ$", "C")

pylab.savefig(main.getOutImagePath(__file__))
