import numpy as np
import pylab
from mpl_toolkits.mplot3d import Axes3D


def plot(x, y, f):
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = [map(f, x, y) for (x, y) in zip(xgrid, ygrid)]
    fig = pylab.figure()
    #TODO ax = fig.gca(projection='3d')
    Axes3D(fig).plot_surface(xgrid, ygrid, zgrid, rstride=1, cstride=1, color="#999999")