import numpy as np
from planar import Planar
import pylab
import main

xmin = -10
xmax = 10
ymin = -10
ymax = 10
planar = Planar(open('matrix/dump2d.csv', 'rb'))


def drawMap():
    return [[planar.func(x, y) for x in range(xmin, xmax + 1)] for y in range(ymin, ymax + 1)]

x = np.arange(xmin, xmax + 1, 1)
y = np.arange(ymin, ymax + 1, 1)

CS = pylab.contour(x, y, drawMap(), (0.01, 0.05, 0.1, 0.15, 0.2, 0.25), colors='k')
pylab.clabel(CS, fontsize=9, inline=1)
pylab.savefig(main.getOutImagePath(__file__))


