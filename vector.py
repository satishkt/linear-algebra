from operator import sub
from functools import reduce
import math
import numpy as np
class Vector(object):
    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates=coordinates
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be non empty')
        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def __str__(self):
        return 'Vector : {} '.format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __plus__(self,other):
        lists=[self.coordinates,other.coordinates]
        new_coordinates = (sum(x) for x in zip(*lists))
        return Vector(list(new_coordinates))

    def __minus__(self,other):
        new_coordinates = [a-b for a,b in zip(self.coordinates,other.coordinates)]
        return Vector(new_coordinates)

    def __scalar_multiply__(self,scalar):
        new_coordinates = [scalar*a for a in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        return  np.sqrt(sum(i*i for i in self.coordinates))

    def direction(self):
        mg = 1.0/(self.magnitude())
        return self.__scalar_multiply__(mg)

    def dotproduct(self,other):
        return sum([a*b for a,b in zip(self.coordinates,other.coordinates)])

    def angler(self,other):
        dot_prod = self.dotproduct(other)
        mag1 = self.magnitude()
        mag2 = other.magnitude()
        return math.acos(dot_prod/(mag1*mag2))

    def angled(self,other):
        return math.degrees(self.angler(other))




my_vector = Vector([1,2,3])
print(my_vector)

my_vector2 = Vector([1,2,3])
my_vector3 = Vector([-1,2,3])

print(my_vector==my_vector2)

print(my_vector3==my_vector)

print(my_vector.__plus__(my_vector))
print (my_vector.__minus__(my_vector))
print (my_vector.__scalar_multiply__(10))

print(my_vector.magnitude())

print(my_vector.direction())



v = Vector([-0.221,7.437])
print(v.magnitude())
v1=Vector([8.813,-1.331,-6.247])
print(v1.magnitude())

v2 =Vector([5.581,-2.136])
print(v2.direction())

v3= Vector([1.996,3.108,-4.554])
print(v3.direction())


x1=Vector([7.887,4.138])
x2=Vector([-8.802,6.776])

print(x1.dotproduct(x2))

a1=Vector([-5.955,-4.904,-1.874])
a2=Vector([-4.496,-8.755,7.103])
print(a1.dotproduct(a2))

b1=Vector([3.183,-7.627])
b2=Vector([-2.668,5.319])

print(b1.angler(b2))

c1=Vector([7.35,0.221,5.188])
c2=Vector([2.751,8.259,3.985])

print(c1.angled(c2))