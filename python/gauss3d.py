# coding=utf-8
from gauss import Gauss
import numpy as np
import pylab
import main
import wg_plot.plot3d as plot3d

x = np.arange(main.xmin, main.xmax, 1)
y = np.arange(main.ymin, main.ymax, 1)
plot3d.plot(x, y, Gauss(4.5, 4.5, 0, 0).gauss)
pylab.savefig(main.getOutImagePath(__file__))