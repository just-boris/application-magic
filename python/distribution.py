# coding=utf-8
from itertools import cycle
import pylab
import numpy as np
import main
from gauss import GaussX

line_cycle = cycle(["-", "-.", "--", ":"])
x_range = np.arange(main.xmin, main.xmax, 0.1)
for (name, r) in main.wg_radius.items():
    inputW = GaussX(r, 0)
    pylab.plot(x_range, [inputW.func(x) for x in x_range], 'k'+next(line_cycle), label=name)
pylab.grid()
pylab.legend()
pylab.savefig(main.getOutImagePath(__file__))
