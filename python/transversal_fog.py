# coding=utf-8
import pylab
import numpy as np
import main
from wg_base.coupling import coupling
from gauss import Gauss
from planar import Planar

outputW = Planar(open('matrix/dump2d.csv'))
r = main.wg_radius['FOG']

def substrat(x):
    inputW = Gauss(r, r, 0, x)
    result = coupling(inputW.func, outputW.func)
    if result > substrat.maxVal:
        substrat.maxVal = result
        substrat.maxArg = r
    return result
substrat.maxVal = 0

xmin = main.xmin
xmax = main.xmax
maxVal = 0

x = np.arange(xmin, xmax, 0.1)
pylab.plot(x, map(substrat, x))
pylab.annotate("Cmax = {0:.3f}".format(substrat.maxVal), (5, 0.75))
main.arrow_axes((xmin, xmax), (0, 1), "$\Delta x$", "C")

pylab.savefig(main.getOutImagePath(__file__))
