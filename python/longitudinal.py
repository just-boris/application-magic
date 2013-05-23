# coding=utf-8
import main
import numpy as np
import pylab
from wg_base.coupling import coupling
from wg_base.divergence import divergence
from planar import Planar
from gauss import Gauss

planar = Planar(open('matrix/dump2d.csv'))
r = main.wg_radius[u'ОВССП']
w = (r, r)
lam = 1.55
n = 1.47

xmin = 0
xmax = 50


def traversal(d):
    w1 = divergence(w, d, lam)
    cylinder = Gauss(*w1, a=0, b=main.max_coupling_point)
    return coupling(planar.func, cylinder.func)

x = np.arange(xmin, xmax+1, 1)
pylab.plot(x, map(traversal, x), 'g')
pylab.grid()
main.arrow_axes((xmin, xmax), (0, 1), "$\Delta z$", "C")

pylab.savefig(main.getOutImagePath(__file__))