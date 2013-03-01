# coding=utf-8
import pylab
import numpy as np
import main
from wg_base.coupling import couplingX
from gauss import GaussX

outputW = GaussX(4, 0)

def substrat(x):
    inputW = GaussX(4, x)
    return couplingX(inputW.gauss, outputW.gauss)

x = np.arange(-20, 20, 0.1)
pylab.plot(x, map(substrat, x))
pylab.annotate("Cmax = {0:.3f}".format(substrat(0)), (5, 0.75))
main.arrow_axes((-20, 20), (0, 1), "$\Delta x$", "C")

pylab.savefig(main.getOutImagePath(__file__))
