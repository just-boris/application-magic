# coding=utf-8
import pylab
import scipy.integrate as integrate
import numpy as np
import main
from wg_base.coupling import couplingX
from gauss import GaussX

outputW = GaussX(4.5, 0)

def substrat(x):
    inputW = GaussX(4.5, x)
    return couplingX(inputW.gauss, outputW.gauss)

x = np.arange(-20, 20, 0.1)
pylab.plot(x, map(substrat, x))

arrowprops = dict(
    clip_on=False,  # plotting outside axes on purpose
    arrowstyle="<-",
    facecolor='k'
)

pylab.annotate("", (-20, 0), xytext=(21, 0), arrowprops=arrowprops)  # абсцисса
pylab.annotate("Δx", (-20, 0), xytext=(21, 0))  # подпись к ней
pylab.annotate("", (-20, 0), xytext=(-20, 1.25), arrowprops=arrowprops)  # ордината
pylab.annotate("C", (-20, 0), xytext=(-20, 1.25))  # подпись к ней

pylab.savefig(main.getOutImagePath(__file__))
