# coding=utf-8
import math
import main
import numpy as np
import pylab
from python.wg_base.frenel import reflection
from wg_base.coupling import coupling
from planar import Planar
from gauss import Gauss

r = main.wg_radius[u'ОВССП']
w = (r, r)
lam = 1.55
n = 1.47

planar = Planar(open('matrix/dump2d.csv'))
reflection_cylinder = Gauss(*w, a=0, b=main.max_coupling_point)

div_angle = 2 * lam / (math.pi * r ** 2)
fi_min = 0
fi_max = 20

def toRadians(fi):
    return fi * math.pi / 180

def backreflection(fi):
    d = 2 * toRadians(fi / 2) * r / div_angle
    cylinder = Gauss(*w, a=0, b=main.max_coupling_point - d)
    return coupling(reflection_cylinder.func, cylinder.func)

x_range = np.arange(fi_min, fi_max, 0.1)
pylab.plot(x_range, [reflection(toRadians(x), 1.47, 2.14) * backreflection(x) for x in x_range], 'k')
pylab.grid()
main.arrow_axes((fi_min, fi_max), (0, 0.05), "$\phi,{}^\circ$", "C")

pylab.savefig(main.getOutImagePath(__file__))
