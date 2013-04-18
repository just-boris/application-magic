# coding=utf-8
import pylab
import numpy as np
import main
from wg_base.coupling import couplingX
from gauss import GaussX
from planar import PlanarX

outputW = PlanarX(open('matrix/dump1d.csv'))

def substrat(x):
    global maxVal
    inputW = GaussX(3, x)
    result = couplingX(inputW.func, outputW.func)
    maxVal = max(result, maxVal)
    return result

xmin = main.xmin
xmax = main.xmax
maxVal = 0

x = np.arange(xmin, xmax, 0.1)
pylab.plot(x, map(substrat, x))
pylab.annotate("Cmax = {0:.3f}".format(maxVal), (5, 0.75))
main.arrow_axes((xmin, xmax), (0, 1), "$\Delta x$", "C")

pylab.savefig(main.getOutImagePath(__file__))
