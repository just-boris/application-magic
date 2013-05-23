# coding=utf-8
import math
import pylab
import numpy as np
import main
from wg_base.coupling import coupling
from scipy.optimize import fmin_powell
from gauss import Gauss
from planar import Planar

planar = Planar(open('matrix/dump2d.csv'))

def annotateWaveguide(name, text_position):
    x = main.wg_radius[name]
    y = var_radius(main.wg_radius[name])
    pylab.plot(x, y, 'bo')
    pylab.annotate(name, xy=(x, y),  xycoords='data', xytext=text_position, textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", connectionstyle="arc,angleA=180,armA=50,rad=8"))

def intersect(r, x):
    cylinder = Gauss(r, r, x[0], x[1])
    return coupling(planar.func, cylinder.func)

def var_radius(r):
    result = intersect(r, fmin_powell(lambda x: -intersect(r, x), [0, -2]))
    if result > var_radius.maxVal:
        var_radius.maxVal = result
        var_radius.maxArg = r
    return result
var_radius.maxVal = 0

xmin = 1
xmax = 7

cutoff_radius = 2.405/(2*math.pi*0.14)

x_range = np.arange(xmin, xmax+1, 0.2)
pylab.plot(x_range, [var_radius(x) for x in x_range], 'k')
# pylab.plot([cutoff_radius, cutoff_radius], [0, 1], 'b--')
annotateWaveguide('Corning', (40, 40))
annotateWaveguide(u'ОВССП', (40, 60))
annotateWaveguide('PANDA', (40, 50))
pylab.grid()
pylab.annotate("Cmax = {0:.3f}".format(var_radius.maxVal), (3, 1))
pylab.annotate("Rmax = {0:.1f}".format(var_radius.maxArg), (3, 0.9))
main.arrow_axes((xmin, xmax), (0, 1.2), "$r$", "C")

pylab.savefig(main.getOutImagePath(__file__))