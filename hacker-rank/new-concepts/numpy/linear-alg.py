#The linalg.det tool computes the determinant of an array.

import numpy
print(numpy.linalg.det([[1 , 2], [2, 1]]))       #Output : -3.0



#The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print(vals)                                      #Output : [ 3. -1.]
print(vecs)                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]


#The linalg.inv tool computes the (multiplicative) inverse of a matrix.
print(numpy.linalg.inv([[1 , 2], [2, 1]]))       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]


                                


import numpy as np

n = int(input())
A = np.array([input().split() for _ in range(n)], float)

print(round(np.linalg.det(A), 2))
