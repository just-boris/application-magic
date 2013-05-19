# coding=utf-8
import math
import main
import numpy as np
import pylab
from wg_base.coupling import coupling
from planar import Planar
from gauss import Gauss

r = main.wg_radius['FOG']
w = (r, r)
lam = 1.55
n = 1.47

planar = Planar(open('matrix/dump2d.csv'))
reflection_cylinder = Gauss(*w, a=0, b=main.max_coupling_point)

div_angle = 2 * lam/(math.pi * r**2)
fi_min = 0
fi_max = 12

def toRadians(fi):
    return fi*math.pi/180

def transmission(fi):
    d = 2*toRadians(fi)*r/div_angle
    cylinder = Gauss(*w, a=d, b=main.max_coupling_point)
    return coupling(planar.func, cylinder.func)*(1-backreflection(fi))

def backreflection(fi):
    d = 2*toRadians(fi/2)*r/div_angle
    cylinder = Gauss(*w, a=0, b=main.max_coupling_point-d)
    return coupling(reflection_cylinder.func, cylinder.func)

x = np.arange(fi_min, fi_max, 0.1)
pylab.plot(x, map(transmission, x), 'k', label=u'Передача')
pylab.plot(x, map(backreflection, x), 'k--', label=u'Отражение')
pylab.legend()
main.arrow_axes((fi_min, fi_max), (0, 1), "$\phi,{}^\circ$", "C")

pylab.savefig(main.getOutImagePath(__file__))
