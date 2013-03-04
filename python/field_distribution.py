import pylab
import numpy as np
import main
from gauss import GaussX

inputW = GaussX(7, 0)

x = np.arange(main.xmin, main.xmax, 0.1)
pylab.plot(x, map(inputW.gauss, x), 'k')
pylab.savefig(main.getOutImagePath(__file__))
