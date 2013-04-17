import main
import numpy as np
import pylab
from wg_base.coupling import coupling
from wg_base.divergence import divergence
from planar import Planar
from gauss import Gauss

planar = Planar(open('python/matrix/dump2d.csv'))
w = (3, 3)
lam = 1.55
n = 1.47

xmin = 0
xmax = 40


def traversal(d):
    w1 = divergence(w, d, n, lam)
    cylinder = Gauss(*w1, a=0, b=-2.98)
    return coupling(planar.func, cylinder.func)

x = np.arange(xmin, xmax, 0.1)
pylab.plot(x, map(traversal, x), 'g')
main.arrow_axes((xmin, xmax), (0, 1), "$\Delta z$", "C")

pylab.savefig(main.getOutImagePath(__file__))