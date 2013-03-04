import pylab
import numpy as np
import main
from gauss import GaussX

inputW = GaussX(7, 0)
outputW = GaussX(7, 4)


x = np.arange(main.xmin, main.xmax, 0.1)
pylab.plot(x, map(inputW.gauss, x), 'k')
pylab.plot(x, map(outputW.gauss, x), 'r')
pylab.savefig(main.getOutImagePath(__file__))
