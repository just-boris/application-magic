import pylab
import numpy as np
import main
from gauss import GaussX

inputW = GaussX(7, 0)


x = np.arange(-20, 20, 0.1)
pylab.plot(x, map(inputW.gauss, x), 'k')
pylab.savefig(main.getOutImagePath(__file__))
