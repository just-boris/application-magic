# coding=utf-8
import pylab
import numpy as np
import main
from gauss import GaussX


delta = 5
inputW = GaussX(main.wg_radius[u'ОВССП'], 0)
outputW = GaussX(main.wg_radius[u'ОВССП'], delta)

def intensity(function):
    return lambda x: function(x)**2

x_range = np.arange(main.xmin, main.xmax+delta, 0.1)
pylab.plot(x_range, [intensity(inputW.func)(x) for x in x_range], 'k', label=u'Входное волокно')
pylab.plot([0, 0], [0, 1], '-.')
pylab.plot(x_range, [intensity(outputW.func)(x) for x in x_range], 'k--', label=u'Выходное волокно')
pylab.plot([delta, delta], [0, 1], '-.')
pylab.grid()
pylab.savefig(main.getOutImagePath(__file__))