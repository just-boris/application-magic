import pylab
import numpy as np
import main
from gauss import GaussX

inputW = GaussX(main.wg_radius['Corning'], 0)

x = np.arange(main.xmin, main.xmax, 0.1)
pylab.plot(x, map(inputW.func, x), 'k')
pylab.savefig(main.getOutImagePath(__file__))
