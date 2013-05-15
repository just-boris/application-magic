from math import sqrt
import numpy as np
from planar import Planar
import pylab
import main

xmin = -10
xmax = 10
ymin = -10
ymax = 10
planar = Planar(open('matrix/dump2d.csv', 'rb'))

def canal(x):
    return -8*sqrt(1-x*x/36)

def drawMap(xrange, yrange):
    return [[planar.func(x, y) for x in xrange] for y in yrange]

x = np.arange(xmin, xmax + 1, 0.5)
y = np.arange(ymin, ymax + 1, 0.5)

canalRange = np.arange(-6, 6.1, 0.1)

CS = pylab.contour(x, y, drawMap(x, y), (0.01, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9), colors='k')
pylab.clabel(CS, fontsize=9, inline=1)
pylab.plot([xmin, xmax], [0, 0], 'k--')
pylab.plot(canalRange, map(canal, canalRange), 'k--')
pylab.savefig(main.getOutImagePath(__file__))