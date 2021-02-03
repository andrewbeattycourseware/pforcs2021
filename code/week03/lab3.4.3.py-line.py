# program takes a list of points 
# and prints out the distance to the origin for each
# Author: Andrew Beatty
import math

points = [(1,2),(3,3),(4,3)]

for x , y in points:
    dist = math.sqrt(x**2 + y**2)
    print ('point({},{}) is {:.2f} , from the origin'.format(x,y,dist))