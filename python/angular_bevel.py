# coding=utf-8
import math
import main
import numpy as np
import pylab
from wg_base.coupling import coupling
from planar import Planar
from gauss import Gauss

planar = Planar(open('matrix/dump2d.csv'))
r = main.wg_radius[u'ОВССП']
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

if __name__ == "__main__":
    x_range = np.arange(fi_min, fi_max, 1)
    pylab.plot(x_range, [angular_xz(x) for x in x_range], 'k', label=u'Плоскость XZ')
    pylab.plot(x_range, [angular_yz(x) for x in x_range], 'k--', label=u'Плоскость YZ')
    pylab.legend()
    pylab.grid()
    main.arrow_axes((fi_min, fi_max), (0, 1), "$\phi,{}^\circ$", "C")

    pylab.savefig(main.getOutImagePath(__file__))