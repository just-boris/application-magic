# coding=utf-8
import pylab
import numpy as np
import main
from gauss import GaussX
from planar import PlanarX

inputW = GaussX(main.wg_radius[u'ОВССП'], -3.5)
outputW = PlanarX(open('matrix/dump1d.csv'))

def intensity(function):
    return lambda x: function(x)**2

x = np.arange(-15, 10, 0.1)
pylab.plot(x, map(intensity(inputW.func), x), 'k', label=u'Волокно')
pylab.plot(x, map(intensity(outputW.func), x), 'k--', label=u'Канальный волновод')
pylab.legend()
pylab.savefig(main.getOutImagePath(__file__))
