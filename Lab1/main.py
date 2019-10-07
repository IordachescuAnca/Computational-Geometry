from collinearity import *

#Input

print("Point A:")
A = Point()
A.readData()

print("Point B:")
B = Point()
B.readData()

print("Point C:")
C = Point()
C.readData()

print("Check the collinearity and write the affine combination if possible.\n")
A.collinearity(B,C)
A.affineCombination(B,C)
