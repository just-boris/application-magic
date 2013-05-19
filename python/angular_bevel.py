# coding=utf-8
import math
import main
import numpy as np
import pylab
from wg_base.coupling import coupling
from planar import Planar
from gauss import Gauss

planar = Planar(open('matrix/dump2d.csv'))
r = main.wg_radius['FOG']
w = (r, r)
lam = 1.55
n = 1.47

fi_min = 0
fi_max = 60

def angular_xz(fi):
    r1 = r/math.cos(fi*math.pi/180)
    cylinder = Gauss(r, r1, a=0, b=main.max_coupling_point)
    return coupling(planar.func, cylinder.func)

def angular_yz(fi):
    r1 = r/math.cos(fi*math.pi/180)
    cylinder = Gauss(r1, r, a=0, b=main.max_coupling_point)
    return coupling(planar.func, cylinder.func)

x = np.arange(fi_min, fi_max, 1)
pylab.plot(x, map(angular_xz, x), 'k', label=u'Ось XZ')
pylab.plot(x, map(angular_yz, x), 'k--', label=u'Ось YZ')
pylab.legend()
main.arrow_axes((fi_min, fi_max), (0, 1), "$\phi,{}^\circ$", "C")

pylab.savefig(main.getOutImagePath(__file__))