import pylab
import numpy as np
import main
from gauss import GaussX
from planar import PlanarX

inputW = GaussX(2, -2)
outputW = PlanarX(open('matrix/dump1d.csv'))


x = np.arange(main.xmin, main.xmax, 0.1)
pylab.plot(x, map(inputW.func, x), 'k')
pylab.plot(x, map(outputW.func, x), 'r')
pylab.savefig(main.getOutImagePath(__file__))
