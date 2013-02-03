# coding=utf-8
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
import numpy as np
import main
from gauss import Gauss

#TODO перенести doPlot в отдельный файл
def doPlot(x, y, f):
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = map(lambda x,y: map(f, x,y), xgrid, ygrid)
    fig = plot.figure()
    Axes3D(fig).plot_surface(xgrid, ygrid, zgrid, rstride=1, cstride=1)

xmin = -20
xmax = 20
ymin = -20
ymax = 20

x = np.arange(xmin, xmax, 1)
y = np.arange(ymin, ymax, 1)
doPlot(x, y, Gauss(4.5, 4.5, 0, 0).gauss)
plot.savefig(main.getOutImagePath(__file__))