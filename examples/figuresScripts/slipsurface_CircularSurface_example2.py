from numpy import array
from pybimstab.slope import NaturalSlope
from pybimstab.slipsurface import CircularSurface
terrainCoords = array(
    [[-2.49, 0.1, 1.7, 3.89, 5.9, 8.12, 9.87, 13.29, 20.29,
      21.43, 22.28, 23.48, 24.65, 25.17],
     [18.16, 17.88, 17.28, 15.73, 14.31, 13.58, 13, 3.61, 3.61,
      3.32, 2.71, 2.23, 1.21, 0.25]])
slope = NaturalSlope(terrainCoords)
surface = CircularSurface(slopeCoords=slope.coords,
                          dist1=7, dist2=20, radius=13)
fig = surface.plot()
