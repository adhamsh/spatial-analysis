
import sys
####The append file path needs to be changed 
sys.path.append('gisalgs')
from worldmap import *

fname = 'data/ne_110m_coastline.shp'
raw_points, numgraticule, numline = prep_projection_data(fname)
print(len(raw_points))
print(numgraticule, numline)
print(raw_points[0])
print(raw_points[3000])

import matplotlib.pyplot as plt
def plot_world(points, numgraticule, numline, color=None):
    ax = plt.gca()
    for i in range(numline):
        if i<numgraticule:
            col = 'lightgrey'
        else:
            col = '#5a5a5a'
            if color is not None:
                col = color
        pts = [[p[1], p[2]] for p in points if p[0]==i]
        l = plt.Polygon(pts, color=col, fill=False, closed=False)
        ax.add_line(l)
        plt.axis('equal') # x and y one the same scale
        ax.axes.get_xaxis().set_visible(False) # don't show axis
        ax.axes.get_yaxis().set_visible(False) # don't show
        ax.set_frame_on(False) # no frame either
#plot_world(raw_points, numgraticule, numline)
#plt.show()

from math import cos, radians, pi
print(cos(pi/2.0))
print(pi)
print(radians(360))
print(radians(180))
print(radians(45))
print(cos(radians(90)))
print(cos(radians(360)))


#Case Study
def transformx(lon, lat):
    if lat>=0:
        x = (lon*(90-lat))/90
    else:
        x = (lon*(90+lat))/90

    y = lat
    return x, y

points=[]
for p in raw_points:
    p1 = transformx(p[1], p[2])
    points.append([p[0], p1[0], p1[1]])
plot_world(points, numgraticule, numline)
plt.show()

##
def transform_equirectangular(lon, lat, lat0=60):
    x = lon * cos(radians(lat0))
    y = lat
    return x, y
print(transform_equirectangular(-83, 40))
 
points=[]
for p in raw_points:
    p1 = transform_equirectangular(p[1], p[2])
    points.append([p[0], p1[0], p1[1]])
plot_world(points, numgraticule, numline)
plt.show()





