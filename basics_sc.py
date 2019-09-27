https://pythonhosted.org/scikit-fuzzy/
https://www.guru99.com/numpy-tutorial.html

import numpy as np

st=np.dtype([('name','S20'),('age','i1')])
a= np.array([('abc',20)], dtype=st)
print(a)


#zeros and ones
np.zeros((2,2))

np.zeros((2,2), dtype=np.int16)

np.ones((2,2))


#reshaping and flatten
e  = np.array([(1,2,3), (4,5,6)])
print(e)
e.reshape(3,2)
e.flatten()

## Horitzontal Stack

f = np.array([1,2,3])
g = np.array([4,5,6])

print('Horizontal Append:', np.hstack((f, g)))


f = np.array([1,2,3])
g = np.array([4,5,6])

print('Vertical Append:', np.vstack((f, g)))


## Generate random nmber from normal distribution
#Loc: the mean. The center of distribution
#scale: standard deviation.
#Size: number of returns

normal_array = np.random.normal(5, 0.5, 10)
print(normal_array)

#Using asarray
A = np.matrix(np.ones((4,4)))
print(A)
np.array(A)[2]=2 #Matrices are immutable
print(A)
np.asarray(A)[2]=2
print(A)

#numpy.arange

Start: Start of interval
Stop: End of interval
Step: Spacing between values. Default step is 1
np.arange(1, 11)
np.arange(1, 14, 4)	
