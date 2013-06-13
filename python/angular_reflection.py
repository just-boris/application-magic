# coding=utf-8
import math
import main
import numpy as np
import pylab
from python.wg_base.frenel import transmission
from wg_base.coupling import coupling
from planar import Planar
from gauss import Gauss

planar = Planar(open('matrix/dump2d.csv'))
r = main.wg_radius[u'ОВССП']
w = (r, r)
lam = 1.55
n_fiber = 1.47
n_canal=2.14

fi_min = 0
fi_max = 60

def toRadians(fi):
    return fi * math.pi / 180

def angular(fi):
    r1 = r / math.cos(fi * math.pi / 180)
    cylinder = Gauss(r, r1, a=0, b=main.max_coupling_point)
    return coupling(planar.func, cylinder.func)

if __name__ == "__main__":
    x_range = np.arange(fi_min, fi_max+1, 1)
    pylab.plot(x_range, [transmission(toRadians(x), n_fiber, n_canal) * angular(x) for x in x_range], 'k',
               label=u'Эффективность стыковки с учетом пропускания')
    pylab.plot(x_range, [transmission(toRadians(x), n_fiber, n_canal) for x in x_range], 'k--', label=u'К-т пропускания')
    pylab.legend(loc='lower right')
    pylab.grid()
    main.arrow_axes((fi_min, fi_max), (0, 1), "$\phi,{}^\circ$", "C")

    pylab.savefig(main.getOutImagePath(__file__))