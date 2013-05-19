import pylab
import numpy as np
import main
from gauss import GaussX

inputW = GaussX(main.wg_radius['FOG'], 0)
outputW = GaussX(main.wg_radius['FOG'], 4)

def intensity(function):
    return lambda x: function(x)**2

x = np.arange(main.xmin, main.xmax, 0.1)
pylab.plot(x, map(intensity(inputW.func), x), 'k')
pylab.plot(x, map(intensity(outputW.func), x), 'k--')
pylab.savefig(main.getOutImagePath(__file__))