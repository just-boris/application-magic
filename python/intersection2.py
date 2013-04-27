import pylab
import numpy as np
import main
from gauss import GaussX
from planar import PlanarX

inputW = GaussX(main.wg_radius['FOG'], -3.5)
outputW = PlanarX(open('matrix/dump1d.csv'))


x = np.arange(-15, 10, 0.1)
pylab.plot(x, map(inputW.func, x), 'k')
pylab.plot(x, map(outputW.func, x), 'r')
pylab.savefig(main.getOutImagePath(__file__))
