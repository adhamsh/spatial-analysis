
########Imports ############
import sys
sys.path
from point import *
from extent import *
from kdtree1 import *
from kdtree2b import *
from math import sqrt, pi
import matplotlib.pyplot as plt
import numpy as np
import random


############ We will be usging GDAL to read the Airport shapefile########
from osgeo import ogr



############### K Cluster Analysis Functions ######################

def kfunc(tree, p, d, density):
    """
    Input
      tree:    a k-D tree
      p:       a point where the K-function is computed
      d:       radius of the circle around p
      density: density of points in the area

    Return
      n: count of points in the circle
      ld: L(d) value
    """
    neighbors = []
    range_query_circular(tree, p, d, neighbors)
    n = len(neighbors)
    kd = float(n)/density
    ld = sqrt(kd/pi)
    return n, ld

def kfunc_monte_carlo(n, area, radii, density, rounds=100):
    """
    Input
      n:            number of points
      area:         Extent object defining the area
      radii:        list containing a set of radii of circles
      density:      density of point events in the area
      rounds:       number of simulations
    Return
      percentiles:  a list of 2.5th and 97.5th percentiles
                    for each d in radii
    """
    alllds = []
    for test in range(rounds):
        points = [ Point(random.uniform(area.xmin, area.xmax),
                         random.uniform(area.ymin, area.ymax))
                   for i in range(n) ]
        t = kdtree2(points)
        lds = [0 for d in radii]
        for i, d in enumerate(radii):
            for p in points:
                ld = kfunc(t, p, d, density)[1]
                lds[i] += ld
        lds = [ld/n for ld in lds]
        alllds.append(lds)
    alllds = np.array(alllds)
    percentiles = []
    for i in range(len(radii)):
        percentiles.append([np.percentile(alllds[:,i], 2.5),
                            np.percentile(alllds[:,i], 97.5)])
    return percentiles

def k_function_test(points, area):
    """
    Input
      points: a list of Point objects
      area: an Extent object

    Return
      ds: list of radii
      percentiles: Monte Carlo result of using radii in ds
      lds: L(d) values for each radius in ds
    """
    n = len(points)
    density = n/area.area()
    t = kdtree2(points)
    d = min([area.xmax-area.xmin,area.ymax-area.ymin])*2/3/10
    ds = [ d*(i+1) for i in range(10)]
    lds = [0 for d in ds]
    for i, d in enumerate(ds):
        for p in points:
            ld = kfunc(t, p, d, density)[1]
            lds[i] += ld
    lds = [ld/n for ld in lds]
    percentiles = kfunc_monte_carlo(n, area, ds, density)
    return ds, percentiles, lds


###################################################################


#Use the ogr to get shapefile
driver = ogr.GetDriverByName("ESRI Shapefile")


##Our file
file_name = 'airport/airprtx010g.shp'
airport_points = driver.Open(file_name, 0)

#Airport shapfile features
airport_features = airport_points.GetLayer(0)

#These are airport points
air_pp = []
for i in range(airport_features.GetFeatureCount()):
     ap = airport_features.GetFeature(i)
     geometry = ap.GetGeometryRef()
     air_pp.append(Point(geometry.GetPoint(0)[0], geometry.GetPoint(0)[1]))


#Extent and area
extent = airport_features.GetExtent()
area = Extent(extent[0], extent[1], extent[2], extent[3])

#Draw the points for the airports
def draw_points(pts, area, color='grey', edgecolor='none', alpha=0.7):
     fig, axis = plt.subplots()
     axis.scatter([p.x for p in pts], [p.y for p in pts], edgecolor=edgecolor, color=color, alpha=alpha)
     plt.xlabel('miles')
     plt.title('United States Airports')
     plt.grid()

     #area extent
     plt.xlim(extent[0], extent[1])
     plt.ylim(extent[2], extent[3])
     axis.set_aspect(1)
     plt.show()

#Call draw function
draw_points(air_pp, area)


#n = amount of airports
n = len(air_pp)

# K Function Test Function call
ds, percentiles, lds = k_function_test(air_pp, area)


#plot the k function results
fig, ax = plt.subplots()
#Green envelopes
plt.plot(ds, [p[1] for p in percentiles], color='green', label='Envelope')
plt.plot(ds, [p[0] for p in percentiles], color='green', label='Envelope')
#Blue airport observations
plt.plot(ds, lds, color='blue', label='Airports')
#Predicted l(d) values
plt.plot([0, plt.xlim()[1]], [0, plt.xlim()[1]], color='red', label='L(d)')

plt.legend(loc='right', bbox_to_anchor=(1.55, 1.0))

plt.xlabel('Radius')
plt.ylabel('L(d)')
ax = plt.gca()
ax.set_aspect(1)
plt.show()

###Test##
#Print points
##for i, v in enumerate(percentiles):
##     print(ds[i], v[0], lds[i], v[1])

