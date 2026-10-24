# transpose
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print(numpy.transpose(my_array))

#flAtten
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print(my_array.flatten())

#Output
#[1 2 3 4 5 6]


#answer
import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)

print(np.transpose(arr))
print(arr.flatten())
