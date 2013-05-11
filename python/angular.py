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

xmin = 0
xmax = math.pi/3

def angular_xz(fi):
    r1 = r/math.cos(fi)
    cylinder = Gauss(r, r1, a=0, b=-2.98)
    return coupling(planar.func, cylinder.func)

def angular_yz(fi):
    r1 = r/math.cos(fi)
    cylinder = Gauss(r1, r, a=0, b=-2.98)
    return coupling(planar.func, cylinder.func)

x = np.arange(xmin, xmax, 0.1)
pylab.plot(x, map(angular_xz, x), 'k')
pylab.plot(x, map(angular_yz, x))
main.arrow_axes((xmin, xmax), (0, 1), "$\phi,rad$", "C")

pylab.savefig(main.getOutImagePath(__file__))