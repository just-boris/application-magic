# coding=utf-8
import os.path as path
import pylab

#axes range
xmin = -10
xmax = 10
ymin = -10
ymax = 10
pylab.rc('font', **{'family': 'arial'})
wg_radius = {
    'Corning': 5.35,
    'FOG': 4.65,
    'PANDA': 4.75
}
max_coupling_point = -4.8

def getOutImagePath(filename):
    directory, filename = path.split(filename)
    return path.normpath(path.join(directory, "../img", path.splitext(filename)[0] + ".png"))


def arrow_axes(xlim, ylim, xtext, ytext):
    """строит координатные оси со стрелкой и подписями в текущей области"""
    arrowprops = dict(clip_on=False, arrowstyle="<-", facecolor='k')
    x_ext = (xlim[1] - xlim[0]) * 1.05 + xlim[0]  # отступ для стрелки
    y_ext = (ylim[1] - ylim[0]) * 1.05 + ylim[0]  # отступ для стрелки
    pylab.annotate("", (xlim[0], ylim[0]), xytext=(x_ext, ylim[0]), arrowprops=arrowprops)  # абсцисса
    if not xtext is None:
        pylab.annotate(xtext, (xlim[0], ylim[0]), xytext=(x_ext, ylim[0]), fontsize=20)  # подпись абсциссы

    pylab.annotate("", (xlim[0], ylim[0]), xytext=(xlim[0], y_ext), arrowprops=arrowprops)  # ордината
    if not ytext is None:
        pylab.annotate(ytext, (xlim[0], ylim[0]), xytext=(xlim[0], y_ext), fontsize=20)  # подпись к ней
    pylab.xlim(xlim[0], xlim[1])
    pylab.ylim(ylim[0], ylim[1])


#unit test
if __name__ == "__main__":
    print getOutImagePath(__file__)
